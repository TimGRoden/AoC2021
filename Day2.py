f = open('input.txt')
datain = [x.split() for x in f.readlines()]
datasafe=[]
for line in datain:
  datasafe.append([line[0],int(line[1])])

def part1():
  pos = [0,0]
  for move in datasafe:
    if move[0] =="up":
      pos[0] -=move[1]
    elif move[0]=="down":
      pos[0] +=move[1]
    else:
      pos[1] += move[1]
  return str(pos[0]*pos[1])
print("Part 1 Solution is "+part1())

def part2():
  pos = [0,0,0]
  for move in datasafe:
    if move[0] =="up":
      pos[2] -=move[1]
    elif move[0]=="down":
      pos[2] +=move[1]
    else:
      pos[1] += move[1]
      pos[0] += move[1]*pos[2]
  return str(pos[0]*pos[1])
print("Part 1 Solution is "+part2())
