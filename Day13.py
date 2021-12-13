f = open('input.txt')
#instruct = [['y',7],['x',5]]
instruct = [['x',655],['y',447],['x',327],['y',223],['x',163],['y',111],['x',81],['y',55],['x',40],['y',27],['y',13],['y',6],['y',0]]
datain = [x.replace('\n','').split(',') for x in f.readlines()]
f.close()
datasafe = []
for line in datain:
  [xin,yin] = line
  datasafe.append([int(xin),int(yin)])

def xref(space,loc):
  newspace = []
  for i in range(len(space)):
    [x1,y1] = space.pop(0)
    if x1>loc:
      x1 = loc*2 - x1
    if [x1,y1] not in newspace: newspace.append([x1,y1])
  return newspace

def yref(space,loc):
  newspace = []
  for i in range(len(space)):
    [x1,y1]=space.pop(0)
    if y1>loc:
      y1 = loc*2 - y1
    if [x1,y1] not in newspace: newspace.append([x1,y1])
  return newspace

out1 = xref(datasafe,instruct[0][1])
print("There are",len(out1),"points left for part 1.")
datasafe = []
for line in datain:
  [xin,yin] = line
  datasafe.append([int(xin),int(yin)])

def fullfold(space,instruct):
  f = open('output.txt',"w")
  for instr in instruct:
    if instr[0]=='x': space = xref(space,instr[1])
    else: space = yref(space,instr[1])
  for line in space: 
    output = str(line[0])+","+str(line[1])+"\n"
    f.write(output)
  f.close()
  return space

out2 = fullfold(datasafe,instruct)
print("Finished writing coordinates to file. Check there!")
