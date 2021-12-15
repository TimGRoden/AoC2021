import time

f = open('testinput.txt')
datain = [list(x.strip()) for x in f.readlines()]
datasafe = []
for line in datain:
    t1 = []
    for item in line:
        t1.append(int(item))
    datasafe.append(t1)


def A_star(space):
    visited = {}
    unvisited = {(0, 0): 0}
    heur = {(0, 0): 0}
    while (len(space[0]) - 1,
           len(space) - 1) not in visited.keys():  #Main loop
        (xpos, ypos) = min(heur, key=heur.get)
        #h_dist = (len(space[0])+len(space)-xpos-ypos) #Manhattan Heuristic
        h_dist = 0  #If this is on, A_star is just Dijkstra's
        currdist = unvisited[(xpos, ypos)]  #Check the current path length
        been = visited.keys()  #Just to avoid checking things several times
        looking = unvisited.keys()
        if xpos - 1 > 0:  #Not on the left edge
            if (xpos - 1, ypos) not in been:
                newdist = currdist + space[ypos][xpos - 1]
                if (xpos - 1, ypos) in looking:
                    if unvisited[(xpos - 1, ypos)] > newdist:
                        unvisited[(xpos - 1, ypos)] = newdist
                        heur[(xpos - 1, ypos)] = newdist + h_dist
                else:
                    unvisited[(xpos - 1, ypos)] = newdist
                    heur[(xpos - 1, ypos)] = newdist + h_dist
        if ypos - 1 > 0:  #Not on the top edge
            if (xpos, ypos - 1) not in been:
                newdist = currdist + space[ypos - 1][xpos]
                if (xpos, ypos - 1) in looking:
                    if unvisited[(xpos, ypos - 1)] > newdist:
                        unvisited[(xpos, ypos - 1)] = newdist
                        heur[(xpos, ypos - 1)] = newdist + h_dist
                else:
                    unvisited[(xpos, ypos - 1)] = newdist
                    heur[(xpos, ypos - 1)] = newdist + h_dist
        if xpos + 1 < len(space[0]):  #Not on the right edge
            if (xpos + 1, ypos) not in been:
                newdist = currdist + space[ypos][xpos + 1]
                if (xpos + 1, ypos) in looking:
                    if unvisited[(xpos + 1, ypos)] > newdist:
                        unvisited[(xpos + 1, ypos)] = newdist
                        heur[(xpos + 1, ypos)] = newdist + h_dist
                else:
                    unvisited[(xpos + 1, ypos)] = newdist
                    heur[(xpos + 1, ypos)] = newdist + h_dist
        if ypos + 1 < len(space):
            if (xpos, ypos + 1) not in been:  #Not on the top edge
                newdist = currdist + space[ypos + 1][xpos]
                if (xpos, ypos + 1) in looking:
                    if unvisited[(xpos, ypos + 1)] > newdist:
                        unvisited[(xpos, ypos + 1)] = newdist
                        heur[(xpos, ypos + 1)] = newdist + h_dist
                else:
                    unvisited[(xpos, ypos + 1)] = newdist
                    heur[(xpos, ypos + 1)] = newdist + h_dist
        visited[(xpos, ypos)] = currdist
        del heur[(xpos, ypos)]
        del unvisited[(xpos, ypos)]
    print("Final distance to", (len(space[0]) - 1, len(space) - 1), "is",
          visited[(len(space[0]) - 1, len(space) - 1)])
    return visited


space2 = []
for l in range(5):
    for line in datasafe:
        t1 = []
        for k in range(5):
            for item in line:
                t1.append(item + k + l)
        space2.append(t1)
for xpos in range(len(space2[0])):
    for ypos in range(len(space2)):
        if space2[ypos][xpos] != 9:
            space2[ypos][xpos] = space2[ypos][xpos] % 9

print("<<A* P1:>>")
start = time.process_time()
t1 = A_star(datasafe)
print("Total Time Taken: ", round((time.process_time() - start) * 1000000),
      "us.")
print("<<A* P2>>")
start = time.process_time()
t2 = A_star(space2)
print("Total Time Taken: ", round((time.process_time() - start) * 1000000),
      "us.")
