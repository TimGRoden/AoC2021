xmin = 236
xmax = 262
ymin = -78
ymax = -58
#"""

def move(xin,yin,xvel,yvel):
  xout = xin + xvel
  yout = yin + yvel
  if xvel>0: xvel -= 1
  elif xvel<0: xvel += 1
  yvel -= 1
  return (xout,yout,xvel,yvel)

def maxh(xvel,yvel,xmin,ymin,xmax,ymax):
  xcoord = 0
  ycoord = 0
  hmax = 0
  while ycoord+yvel >= ymin and xcoord+xvel <= xmax:
    (xcoord,ycoord,xvel,yvel) = move(xcoord,ycoord,xvel,yvel)
    if ycoord>hmax: hmax = ycoord
  if xcoord<=xmax and xcoord>= xmin and ycoord>=ymin and ycoord <= ymax:
    return hmax
  else:
    return 0

def findmax(xmin,ymin,xmax,ymax):
  best = [0,0,0] #height, xvel, yvel
  for i in range(100):
    for j in range(100):
      hout = maxh(i,j,xmin,ymin,xmax,ymax)
      if hout>best[0]: best = [hout,i,j]
  print("Best height at",best[0],"with vel",(best[1],best[2]))

def landsin(xvel,yvel,xmin,ymin,xmax,ymax):
  xcoord = 0
  ycoord = 0
  while ycoord+yvel >= ymin and xcoord+xvel <= xmax:
    (xcoord,ycoord,xvel,yvel) = move(xcoord,ycoord,xvel,yvel)
  if xcoord<=xmax and xcoord>= xmin and ycoord>=ymin and ycoord <= ymax:
    return True
  else:
    return False

def findsuccess(xmin,ymin,xmax,ymax):
  count = 0
  for i in range(xmax+1):
    yvel = ymin
    while yvel <100:
      success = landsin(i,yvel,xmin,ymin,xmax,ymax)
      if success==True:
        count += 1
      yvel += 1
  return count

findmax(xmin,ymin,xmax,ymax)
print("Found",findsuccess(xmin,ymin,xmax,ymax),"different routes.")
