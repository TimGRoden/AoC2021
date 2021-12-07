f = open('input.txt')
datain = [int(x) for x in f.readlines()[0].split(',')]

def fuelneed(cl,pos):
  fuel = 0
  for crab in cl:
    fuel += abs(crab - pos)
  return fuel

def part1(cl):
  fueldic = {}
  for fuel in range(max(cl)):
    fueldic[fuel] = fuelneed(cl,fuel)
  minpos = min(fueldic, key=fueldic.get)
  minfuel = fueldic[minpos]
  print("Best position is "+str(minpos)+", taking "+str(minfuel)+" fuels.")
part1(datain)

def fuelneed2(cl,pos):
  fuel = 0
  for crab in cl:
    dist = abs(crab - pos)
    fuel += int(dist*(dist+1)/2)
  return fuel

def part2(cl):
  fueldic2 = {}
  for fuel in range(max(cl)):
    fueldic2[fuel] = fuelneed2(cl,fuel)
  minpos = min(fueldic2, key=fueldic2.get)
  minfuel = fueldic2[minpos]
  print("Best new position is "+str(minpos)+", taking "+str(minfuel)+" fuels.")
part2(datain)
