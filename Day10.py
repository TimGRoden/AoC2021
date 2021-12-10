f = open('input.txt')
datasafe = []
for x in f.readlines(): datasafe.append(x.split()[0])

def rem(inp):
  tempy = ""
  dicty = {'[':']','{':'}','(':')','<':'>'}
  for key in dicty.keys():
    setstr = key+dicty[key]
    if setstr in inp:
      tempy = inp.replace(setstr,"")
  if tempy == "": tempy = inp
  if len(tempy)!=len(inp): tempy = rem(tempy)
  return tempy

def solvecorr(inp):
  closes = [')',']','>','}']
  for i in range(len(inp)-1):
    if inp[i+1] in closes:
      if inp[i+1]==')': return 3
      elif inp[i+1]==']': return 57
      elif inp[i+1]=='}': return 1197
      elif inp[i+1]=='>': return 25137
  return 0

def incomplete(inp):
  total = 0
  final = []
  for data in inp:
    t1 = rem(data)
    if (']' not in t1) and ('}' not in t1) and (')' not in t1) and ('>' not in t1):
      incomp = True
    else: incomp = False
    if not incomp: 
      total += solvecorr(t1)
    else: final.append(t1)
  return [total,final]

def solveincompstr(inp):
  dicty = {'[':']','{':'}','(':')','<':'>'}
  solstr = ""
  for char in inp[::-1]:
    solstr += dicty[char]
  total = 0
  scores = {')':1,']':2,'}':3,'>':4}
  for char in solstr:
    total *= 5
    total += scores[char]
  return total

def solveincomp(inp):
  scores = []
  for data in inp:
    scores.append(solveincompstr(data))
  scores.sort()
  while len(scores)>1:
    del scores[0]
    del scores[-1]
  return scores[0]

[total, incomps] = incomplete(datasafe)
print("Final corrupted total:",total)
print("Final incomplete total:",solveincomp(incomps))
