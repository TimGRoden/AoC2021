start1,start2 = 7,4
#start1,start2 = 4,8
class Player:
  def __init__(self,pos):
    self.pos = pos
    self.score = 0
  
  def move(self,dist):
    newpos = self.pos+dist
    if newpos>10: 
      if newpos %10==0:newpos = 10
      else: newpos = newpos %10
    self.pos = newpos
    self.score += self.pos

def game1(start1,start2):
  P1 = Player(start1)
  P2 = Player(start2)
  diceroll = 0
  rolls = 0
  while True:
    move = 0
    rolls += 3
    for i in range(3):
      diceroll += 1
      if diceroll>100: diceroll = 1
      move += diceroll
    P1.move(move)
    if P1.score>=1000:
      output = ("1",P2.score,rolls)
      break
    move = 0
    rolls += 3
    for i in range(3):
      diceroll += 1
      if diceroll>100: diceroll = 1
      move += diceroll
    P2.move(move)
    if P2.score>=1000:
      output = ("2",P1.score,rolls)
      break    
  return output
(winner,loserpos,rolls) = game1(start1,start2)
print("Part 1: ",winner,"wins.",loserpos,"x",rolls,"=",loserpos*rolls)

movelist = []
for i in range(3):
  for j in range(3):
    for k in range(3):
      movelist.append(i+j+k+3)
movedic = {}
for move in movelist:
  if move in movedic.keys():
    movedic[move] += 1
  else: movedic[move] = 1

def dirac(pos1,pos2,sc1,sc2,active,movedic):
  tempresults = [0,0]
  if active==1:
    for key in movedic.keys():
      newpos = pos1 + key
      if newpos>10: newpos = newpos %10
      newscore = sc1 + newpos
      if newscore>=21:
        tempresults[0]+=movedic[key]
      else:
        w1,w2 = dirac(newpos,pos2,newscore,sc2,2,movedic)
        tempresults[0] += w1*movedic[key]
        tempresults[1] += w2*movedic[key]
  else:
    for key in movedic.keys():
      newpos = pos2 + key
      if newpos>10: newpos = newpos %10
      newscore = sc2 + newpos
      if newscore>=21:
        tempresults[1] += movedic[key]
      else:
        w1,w2 = dirac(pos1,newpos,sc1,newscore,1,movedic)
        tempresults[0] += w1*movedic[key]
        tempresults[1] += w2*movedic[key]
  return tempresults

w1,w2 = dirac(start1,start2,0,0,1,movedic)
if w1>w2:print("Player 1 wins more times ("+str(w1)+")")
else: print("Player 2 wins more times ("+str(w2)+")")
print("Player 1:",w1)
print("Player 2:",w2)
