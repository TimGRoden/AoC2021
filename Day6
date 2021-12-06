f = open('input.txt')
datain = f.readlines()
datasafe = [int(x) for x in datain[0].split(',')]

def growdic(fishin):
  fishout = {}
  for key in fishin.keys():
    fishout[key-1] = fishin[key]
  fishout[8] = fishout[-1]
  t1 = fishout[6]
  t1 += fishout[-1]
  fishout[6] = t1
  del fishout[-1]
  return fishout

def part1(fishin,daysin):
  days = 0
  fishdic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
  for fish in datasafe:
    fishdic[fish] += 1
  while days<daysin:
    days += 1
    fishdic = growdic(fishdic)
  count = 0
  for key in fishdic.keys():
    count += fishdic[key]
  print("Final number of fish is after "+str(daysin)+" days is "+str(count)+".")

part1(datasafe,80)
part1(datasafe,256)
