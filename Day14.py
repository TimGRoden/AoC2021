from collections import Counter
f = open('input.txt')
datain = [x.strip().split(' -> ') for x in f.readlines()]
subdic = {}
for line in datain:
  subdic[line[0]] = line[1]

inny = list('HHKONSOSONSVOFCSCNBC')
indic = {}
while len(inny)>1:
  char = inny.pop(0)
  aim = char+inny[0]
  if aim in indic.keys(): indic[aim] += 1
  else: indic[aim] = 1

def dicsub(dicin,subdic):
  newdic = {}
  for key in dicin.keys():
    t1 = key[0]+subdic[key]
    t2 = subdic[key]+key[1]
    if t1 in newdic.keys(): newdic[t1] += dicin[key]
    else: newdic[t1] = dicin[key]
    if t2 in newdic.keys(): newdic[t2] += dicin[key]
    else: newdic[t2] = dicin[key]
  return newdic

def diccopy(indic):
  outdic = {}
  for key in indic.keys():
    outdic[key] = indic[key]
  return outdic

def run2(indic,subdic,steps):
  t1 = diccopy(indic)
  for i in range(steps):
    t1 = dicsub(t1,subdic)
  letterdic = {}
  for key in t1.keys():
    if key[0] in letterdic.keys(): letterdic[key[0]] += t1[key]
    else: letterdic[key[0]] = t1[key]
    if key[1] in letterdic.keys(): letterdic[key[1]] += t1[key]
    else: letterdic[key[1]] = t1[key]
  for key in letterdic.keys():
    if letterdic[key] %2 != 0:
      letterdic[key] +=1
    letterdic[key] = int(letterdic[key]/2)
  minfound = 1000000000000000000000
  maxfound = 0
  for key in letterdic.keys():
    if letterdic[key]<minfound:
      minfound = letterdic[key]
    if letterdic[key]>maxfound:
      maxfound = letterdic[key]
  print("After",steps,"steps:",maxfound,"-",minfound,"=",maxfound-minfound)
  return t1

p1 = run2(indic,subdic,10)
p2 = run2(indic,subdic,40)
