import time
start=time.process_time()
f = open('input.txt')
datain = [list(x) for x in f.readlines()]
datasafe = [[-2]*(len(datain[0])+1)]
for line in datain: 
  if '\n' in line:
    line.remove('\n')
  l1 = [-2]
  for item in line:
    l1.append(int(item))
  l1.append(-2)
  datasafe.append(l1)
datasafe.append([-2]*len(datasafe[1]))

def inc(x,y,space):
  space[y][x]=0                 #Flash!
  for i in range(3):
    for j in range(3):
      if space[y-1+j][x-1+i]>0: #If it hasn't flashed, it glows more.
        space[y-1+j][x-1+i]+=1
        if space[y-1+j][x-1+i]>9: space[y-1+j][x-1+i]=-1
  return space

def listcopy(space):
  newspace = []
  for line in space:
    l1 = []
    for x in line:
      l1.append(x)
    newspace.append(l1)
  return newspace

def timestep(space):
  for x in range(len(space[0])-2):
    for y in range(len(space)-2):
      space[y+1][x+1] += 1
      if space[y+1][x+1]>9: space[y+1][x+1]=-1
  ts1 = listcopy(space)
  ts2 = []
  while ts1 != ts2:
    ts2 = listcopy(ts1)
    for x in range(len(space[0])-2):
      for y in range(len(space)-2):
        if ts1[y+1][x+1]==-1: ts1=inc(x+1,y+1,ts1)
  return ts1

def run1(space,steps):
  t1 = listcopy(space)
  count = 0
  for i in range(steps):
    t1 = timestep(t1)
    for line in t1:
      for val in line:
        if val==0: count += 1
  return count

print("Final flash count for 100 steps is",run1(datasafe,100))

def run2(space):
  t1 = listcopy(space)
  stepcount = 0
  finished = False
  while not finished:
    count = 0
    stepcount += 1
    t1 = timestep(t1)
    for line in t1:
      for val in line:
        if val==0: count += 1
    if count==100:
      finished = True
  print("Found all 0 at",stepcount,"steps.")
  return stepcount

run2(datasafe)

print("Total Time Taken: ",round((time.process_time()-start)*1000000),"us.")
