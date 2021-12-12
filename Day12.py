import queue
f = open('input.txt')
datain = [x.replace('\n','').split('-') for x in f.readlines()]

conn = {}
for line in datain:
  [a1,a2] = line
  conn[a1]=[]
  conn[a2]=[]

for line in datain:
  [p1,p2] = line
  if p1 =='start':
    conn[p1].append(p2)
  elif p2=='start':
    conn[p2].append(p1)
  else:
    conn[p1].append(p2)
    conn[p2].append(p1)
del conn['end']

def listcopy(listin):
  listout = []
  for item in listin: listout.append(item)
  return listout

def add1(listin,conn):
  routes = []
  if listin[-1]!='end':
    for tar in conn[listin[-1]]:
      t1 = listcopy(listin)
      if tar.islower():
        if tar not in listin:
          t1.append(tar)
          routes.append(t1)
      else: 
        t1.append(tar)
        routes.append(t1)
  return routes

def findroutes(conn):
  routes = []
  checks = queue.Queue()
  checks.put(['start'])
  while not checks.empty():
    t1 = checks.get()
    t2 = add1(t1,conn)
    if t2==[]:
      if t1[-1]=='end': routes.append(t1)
    else:
      for opt in t2:
        checks.put(opt)
  return routes

tout = findroutes(conn)
print("Found",len(tout),"routes.")


def add2(listin,conn):
  routes = []
  [smalls,r1]=listin
  if r1[-1]!='end':
    for tar in conn[r1[-1]]:
      t1 = listcopy(r1)
      if tar.islower():
        if t1.count(tar)<smalls:
          t1.append(tar)
          if t1.count(tar)==2 or smalls==1:
            routes.append([1,t1])
          else:
            routes.append([2,t1])
      else: 
        t1.append(tar)
        routes.append([smalls,t1])
  return routes

def findroutes2(conn):
  routes = []
  checks = queue.Queue()
  checks.put([2,['start']])
  while not checks.empty():
    t1 = checks.get()
    t2 = add2(t1,conn)
    if t2==[]:
      if t1[1][-1]=='end': routes.append(t1[1])
    else:
      for opt in t2:
        checks.put(opt)
  return routes

tout = findroutes2(conn)
tout.sort()
print("Found",len(tout),"routes.")
