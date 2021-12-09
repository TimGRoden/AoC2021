f=open('input.txt')
#f=open('testinput.txt')
datain = [list(x) for x in f.readlines()]
datasafe = [[10]*(len(datain[0])+2)]
for line in datain: 
  if '\n' in line:
    line.remove('\n')
  l1 = [10]
  for item in line:
    l1.append(int(item))
  l1.append(10)
  datasafe.append(l1)
datasafe.append([10]*len(datasafe[0]))

def ismin(space, x, y):
  count = 0
  if space[y][x]<space[y+1][x]:
    count += 1
  if space[y][x]<space[y-1][x]:
    count += 1
  if space[y][x]<space[y][x+1]:
    count += 1
  if space[y][x]<space[y][x-1]:
    count += 1
  if count == 4:
    ismin = True
  else: 
    ismin = False
  return ismin
#ismin() returns true if (x,y) is a local minimum.

def part1(space):
  heightsum = 0
  count = 0
  lowdic = {}
  for x in range(len(datasafe[1])-2): #x-coord will be x+1 to ignore bounding box.
    for y in range(len(datasafe)-2): #y-coord will also be y+1.
      if ismin(space,x+1,y+1):
        heightsum += 1 + datasafe[y+1][x+1]
        count += 1
        coord = (x+1,y+1)
        lowdic[coord] = datasafe[y+1][x+1]
  print("A total of "+str(count)+" low points were found.")
  print("Sum of risk is "+str(heightsum)+".")
  return lowdic

lowpoints = part1(datasafe)

def basinfind(space, indic):
  s1 = indic.copy()
  for (x,y) in indic.keys():
    if space[y+1][x]<9 and (x,y+1) not in indic.keys(): #So long as I haven't found an edge, add it.
      s1[(x,y+1)] = space[y+1][x]
    if space[y-1][x]<9 and (x,y-1) not in indic.keys():
      s1[(x,y-1)] = space[y-1][x]
    if space[y][x+1]<9 and (x+1,y) not in indic.keys():
      s1[(x+1,y)] = space[y][x+1]
    if space[y][x-1]<9 and (x-1,y) not in indic.keys():
      s1[(x-1,y)] = space[y][x-1]
  if len(s1) != len(indic):
    s1 = basinfind(space, s1)
  return s1

def part2(space,lows):
  basinsizes=[]
  for (x,y) in lows.keys(): #For every lowpoint that I found...
    basindic = {}
    basindic[(x,y)]=space[y][x]
    basinsizes.append(len(basinfind(space, basindic)))
  total = 1
  for i in range(3): #For the 3 largest basins found.
    total *= basinsizes.pop(basinsizes.index(max(basinsizes)))
    #Adds the largest value to total, and removes it.
  print("Total size of 3 largest basins is "+str(total)+".")

part2(datasafe,lowpoints)
