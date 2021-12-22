f = open('input.txt')
datain = [x.strip().replace("x=","").replace("y=","").replace("z=","").replace(" ",",") for x in f.readlines()]
temp1 = []
for line in datain:temp1.append(line.split(","))
datasafe = []
for inst in temp1:
  line = []
  line.append(inst[0])
  x1,x2 = inst[1].split("..")
  y1,y2 = inst[2].split("..")
  z1,z2 = inst[3].split("..")
  line.append([int(x1),int(x2)])
  line.append([int(y1),int(y2)])
  line.append([int(z1),int(z2)])
  datasafe.append(line)

def initialise(instructions):
  spacedic = {}
  for inst in instructions:
    if (max(inst[1])>=-50) and (min(inst[1])<=50) and (max(inst[2])>=-50) and (min(inst[2])<=50) and (max(inst[3])>=-50) and (min(inst[3])<=50):#A part 1 initialisation.
      for i in range(inst[1][1]-inst[1][0]+1):
        for j in range(inst[2][1]-inst[2][0]+1):
          for k in range(inst[3][1]-inst[3][0]+1):
            if inst[0]=="on":
              spacedic[(inst[1][0]+i,inst[2][0]+j,inst[3][0]+k)] = True
            else:
              target = (inst[1][0]+i,inst[2][0]+j,inst[3][0]+k)
              if target in spacedic.keys():
                del spacedic[target]
  print("Finished instructions from -50 to 50.")
  print("Found",len(spacedic),"cells.")
  return spacedic
initialise(datasafe)

