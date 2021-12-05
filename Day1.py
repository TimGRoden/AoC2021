f = open('input.txt')
datain = [x.split() for x in f.readlines()]
datasafe=[]
for line in datain:
  datasafe.append(int(line[0]))

def increased(i,j):
  return i<j

def part1():
  count = 0
  for i in range(len(datasafe)-1):
    if increased(datasafe[i],datasafe[i+1]):
      count += 1
  print("Total part 1 count: "+str(count))
part1()

def part2():
  count = 0
  for i in range(len(datasafe)-3):
    if increased(datasafe[i],datasafe[i+3]):
      count +=1
  print("Total part 2 count: "+str(count))
part2()
