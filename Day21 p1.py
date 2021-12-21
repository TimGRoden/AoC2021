start1,start2 = 4,8
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
