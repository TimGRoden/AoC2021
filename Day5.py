f = open('input.txt')
datain = [x.split() for x in f.readlines()]

startpoints = []
endpoints = []
for line in datain: #Get the data into the two lists.
  start = line[0].split(',')
  end = line[2].split(',')
  startpoints.append([int(start[0]),int(start[1])])
  endpoints.append([int(end[0]),int(end[1])])

def filterh(l1,l2): #Filter two lists to find all horizontal lines.
  listout = []
  for i in range(len(l1)):
    if l1[i][0]==l2[i][0]:
      listout.append([l1[i],l2[i]])
  return listout

def filterv(l1,l2): #Filter two lists to find all vertical lines.
  listout = []
  for i in range(len(l1)):
    if l1[i][1]==l2[i][1]:
      listout.append([l1[i],l2[i]])
  return listout

def listcopy(l1):
  l2 = []
  for line in l1:
    l2.append(line)
  return l2

def addline(spacedict,line): #Add the new points to the space dict.
  if line[0][0]==line[1][0]: #Vertical Line!
    diff = line[0][1] - line[1][1]
    direc = -1* int(abs(diff)/diff)
    for y in range(abs(diff)+1):
      yval = line[0][1]+y*direc
      xval = line[0][0]
      if (xval,yval) in spacedict:
        spacedict[(xval,yval)] += 1
      else:
        spacedict[(xval,yval)] = 1
  else:                       #Horizontal Line!
    diff = line[0][0] - line[1][0]
    direc = -1*int(abs(diff)/diff)
    for x in range(abs(diff)+1):
      yval = line[0][1]
      xval = line[0][0]+x*direc
      if (xval,yval) in spacedict:
        spacedict[(xval,yval)] += 1
      else:
        spacedict[(xval,yval)] = 1
  return spacedict

def part1():
  spacedict={}
  for inst in filterh(startpoints,endpoints):
    spacedict = addline(spacedict,inst)
  for inst in filterv(startpoints,endpoints):
    spacedict = addline(spacedict,inst)
  count = 0
  for item in spacedict.items():
    if item[1] >1:
      count += 1
  print("Final count of danger tiles for part 1 is "+str(count)+".")
part1()

def addany(spacedict,line): #Add the new points to the space dict.
  if line[0][0]==line[1][0]:            #Vertical Line!
    diff = line[0][1] - line[1][1]
    direc = -1* int(abs(diff)/diff)
    for y in range(abs(diff)+1):
      yval = line[0][1]+y*direc
      xval = line[0][0]
      if (xval,yval) in spacedict:
        spacedict[(xval,yval)] += 1
      else:
        spacedict[(xval,yval)] = 1
  elif line[0][1]==line[1][1]:          #Horizontal Line!
    diff = line[0][0] - line[1][0]
    direc = -1*int(abs(diff)/diff)
    for x in range(abs(diff)+1):
      yval = line[0][1]
      xval = line[0][0]+x*direc
      if (xval,yval) in spacedict:
        spacedict[(xval,yval)] += 1
      else:
        spacedict[(xval,yval)] = 1
  else:                                 #Diagonals, oh no!
    diff_x = line[0][0] - line[1][0]
    dir_x = -1*int(abs(diff_x)/diff_x)
    diff_y = line[0][1] - line[1][1]
    dir_y = -1*int(abs(diff_y)/diff_y)
    for i in range(abs(diff_x)+1):
      yval = line[0][1]+i*dir_y
      xval = line[0][0]+i*dir_x
      if (xval,yval) in spacedict:
        spacedict[(xval,yval)] += 1
      else:
        spacedict[(xval,yval)] = 1
  return spacedict

def part2():
  spacedict={}
  for i in range(len(startpoints)):
    spacedict = addany(spacedict,[startpoints[i],endpoints[i]])
  count = 0
  for item in spacedict.items():
    if item[1]>1:
      count += 1
  print("Final count of danger tiles for part 2 is "+str(count)+".")

part2()
