f = open('input.txt')
initspace = [list(x.strip()) for x in f.readlines()]

def spacecopy(spacein):
  tspace = []
  for line in spacein:
    tline = []
    for point in line:
      tline.append(point)
    tspace.append(tline)
  return tspace

def move(spacein):
  tspace = spacecopy(spacein)
  for y in range(len(spacein)):
    for x in range(len(spacein[0])):
      if spacein[y][x]==">":
        if x==len(spacein[0])-1: target = 0
        else: target = x+1
        if spacein[y][target]==".":
          tspace[y][target]=">"
          tspace[y][x]="."
  t1 = spacecopy(tspace)
  for y in range(len(t1)):
    for x in range(len(t1[0])):
      if t1[y][x]=="v":
        if y==len(t1)-1: target = 0
        else: target = y+1
        if t1[target][x]==".":
          tspace[target][x]="v"
          tspace[y][x]="."
  return tspace

def findstill(spacein):
  steps = 0
  t1 = spacecopy(spacein)
  t2 = []
  while True:
    steps += 1
    if steps%100==0:print("Completed",steps,"steps.")
    t2 = move(t1)
    if t1==t2:
      return (t1,steps)
    else: t1 = spacecopy(t2)

results = findstill(initspace)
print("Still found after",results[1],"steps.")
#for line in results[0]: print(line)
