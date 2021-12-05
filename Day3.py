f=open('input.txt')
datasafe = [x.strip() for x in f.readlines()]

def oppo(gamma):
  epsilon = ""
  for char in gamma:
    if char=="0":
      epsilon += "1"
    else:
      epsilon += "0"
  return epsilon

def part1():
  gamma = ""
  for i in range(len(datasafe[0])):
    found1 = 0
    found0 = 0
    for line in datasafe:
      if line[i]=="1":
        found1 += 1
      else:
        found0 += 1
    if found1>found0:
      gamma += "1"
    else:
      gamma += "0"
  epsilon = oppo(gamma)
  print("<<<<PART 1>>>>")
  print("Gamma: "+gamma)
  print("Epsilon: "+epsilon)
  return [gamma,epsilon]
[gamma,epsilon] = part1()

def listfilter(listy,pos,key):
  matching = []
  for line in listy:
    if line[pos]==key[pos]:
      matching.append(line)
  return matching

def listfilter2(listy,pos,key):
  matching = []
  for line in listy:
    if line[pos]==key:
      matching.append(line)
  return matching

def listcopy(listy):
  out = []
  for line in listy:
    out.append(line)
  return out
print("<<<PART 2>>>")
def OGR():
  i=0
  possible = listcopy(datasafe)
  newlist = []
  found = 0
  while i<len(datasafe[0]) and found == 0:
    found1 = 0
    found0 = 0
    for line in possible:
      if line[i]=="1":
        found1 += 1
      else:
        found0 += 1
    if found1>=found0:
      key = "1"
    else:
      key = "0"
    newlist = listfilter2(possible,i,key)
    if len(newlist)==1:
      print("Oxygen Generator Rating: "+newlist[0])
      found = 1
    else:
      i += 1
      possible = listcopy(newlist)
OGR()

def CSR():
  i=0
  possible = listcopy(datasafe)
  newlist = []
  found = 0
  while i<len(datasafe[0]) and found == 0:
    found1 = 0
    found0 = 0
    for line in possible:
      if line[i]=="1":
        found1 += 1
      else:
        found0 += 1
    if found1<found0:
      key = "1"
    else:
      key = "0"
    newlist = listfilter2(possible,i,key)
    if len(newlist)==1:
      print("CO2 Scrubber Rating: "+newlist[0])
      found = 1
    else:
      i += 1
      possible = listcopy(newlist)
CSR()
