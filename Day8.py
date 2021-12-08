f = open('input.txt')
datain = [x.split(' | ') for x in f.readlines()]

def makedatasafe():
  datasafe = [None]*len(datain)
  for i in range(len(datain)):
    datasafe[i] = [datain[i][0].split(),datain[i][1].split()]
  #Datasafe stored as [line][input/output][value]
  return datasafe
datasafe = makedatasafe()

def part1(readout):
  count = 0
  for line in readout: #For every line we had:
    for item in line[1]: #For every output:
      if len(item) in [2, 3, 4, 7]: #If it meant 1, 4, 7, 8
        count += 1
  print("Final count of 1s, 4s, 7s and 8s is "+str(count)+".")
part1(datasafe)

def sortstr(strin):
  t1 = sorted(strin)
  return "".join(t1)

def sortlist(inputs):
  sorted = []
  for i in range(len(inputs)):
    tin = []
    tout = []
    inputy = inputs[i]
    for j in range(len(inputy[0])): #Deal with the inputs of input i
      t1 = inputy[0][j]
      tin.append(sortstr(t1))
    for j in range(len(inputy[1])): #Deal with the outputs of input i
      tout.append(sortstr(inputy[1][j]))
    sorted.append([tin,tout])
  return sorted
datasort = sortlist(datasafe)

def matchin(key, strin):
  lkey = list(key)
  lstr = list(strin)
  count = 0
  for val in lkey:
    if val in lstr:
      count += 1
  return count

def solveinput(trials,display):
  soldic = {}
  for item in trials: #For each of the attempted values. Pass 1 looking for 1,4,7,8.
    l1 = len(item)
    if l1==2:
      soldic[1] = item
    elif l1==3:
      soldic[7] = item
    elif l1==4:
      soldic[4] = item
    elif l1==7:
      soldic[8] = item
  for item in trials: #Now run trials for 2, 3, 6, 9
    l1 = len(item)
    match4 = matchin(soldic[4],item)
    match1 = matchin(soldic[1],item)
    if match1==1 and l1==6:
      soldic[6]=item
    elif match1==2 and l1==5:
      soldic[3]=item
    elif match4==2 and l1==5:
      soldic[2]=item
    elif match4==4 and l1==6:
      soldic[9]=item
  for item in trials: #Now place 0 and 5.
    l1 = len(item)
    found = soldic.values()
    if l1==5 and item not in found: #Havne't found it yet and it's length 5, it's a 5!
      soldic[5]=item
    elif l1==6 and item not in found:
      soldic[0]=item
  outdic = dict(zip(soldic.values(),soldic.keys()))
  a1 = outdic[display[0]]
  a2 = outdic[display[1]]
  a3 = outdic[display[2]]
  a4 = outdic[display[3]]
  return a1*1000+a2*100+a3*10+a4



def part2(datasorted):
  total = 0
  for item in datasorted: #For each input
    total += solveinput(item[0],item[1]) #Find the sum of values from the outputs
  print("Final total is "+str(total)+".") #Print the final total
part2(datasort)

  
