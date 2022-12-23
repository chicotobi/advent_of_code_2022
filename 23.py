import numpy as np
import collections

d = open("23_example.txt", "r").read().splitlines()
els = []
for (i,line) in enumerate(d):
  for (j,el) in enumerate(line):
    if d[i][j] == '#':
      els.append((i,j))

def check_any(a,i,j):
  v = a[i-1,j-1] or a[i-1,j] or a[i-1,j+1] or a[i,j+1] or a[i+1,j+1] or a[i+1,j] or a[i+1,j-1] or a[i,j-1] 
  return v

def check_north(a,i,j):
  v = np.all(~a[i-1,j-1:j+2])
  goal = (i-1,j)
  return v,goal

def check_south(a,i,j):
  v = np.all(~a[i+1,j-1:j+2])
  goal = (i+1,j)
  return v,goal

def check_west(a,i,j):
  v = np.all(~a[i-1:i+2,j-1])
  goal = (i,j-1)
  return v,goal

def check_east(a,i,j):
  v = np.all(~a[i-1:i+2,j+1])
  goal = (i,j+1)
  return v,goal


def pr(els):
  minx = min(i for (i,j) in els)
  maxx = max(i for (i,j) in els)
  miny = min(j for (i,j) in els)
  maxy = max(j for (i,j) in els)
  for i in range(minx,maxx+1):
    s = ''
    for j in range(miny,maxy+1):
      if (i,j) in els:
        s += '#'
      else:
        s += '.'
    print(s)
  print("Free grid places:",(maxx-minx+1)*(maxy-miny+1)-len(els))
  print()
  
pr(els)

nrounds = 10000
order = [check_north,check_south,check_west,check_east]
for r in range(nrounds):
  goals = {}
  new_els = []
  
  # translate to array
  minx = min(i for (i,j) in els)-1
  maxx = max(i for (i,j) in els)+1
  miny = min(j for (i,j) in els)-1
  maxy = max(j for (i,j) in els)+1
  a = np.full((maxx-minx+1,maxy-miny+1),False)
  for (i,j) in els:
    a[i-minx,j-miny] = True

  for (i,j) in els:
    if check_any(a,i-minx,j-miny):
      v, goal = order[0](a,i-minx,j-miny)
      if v:
        goals[(i,j)] = (goal[0]+minx,goal[1]+miny)
      else:
        v, goal = order[1](a,i-minx,j-miny)
        if v:
          goals[(i,j)] = (goal[0]+minx,goal[1]+miny)
        else:
          v, goal = order[2](a,i-minx,j-miny)
          if v:
            goals[(i,j)] = (goal[0]+minx,goal[1]+miny)
          else:
            v, goal = order[3](a,i-minx,j-miny)
            if v:
              goals[(i,j)] = (goal[0]+minx,goal[1]+miny)
            else:
              new_els += [(i,j)]
    else:
      new_els += [(i,j)]     
  
  # Move order
  order = order[1:] + [order[0]]
  
  # Execute possible goals
  pos_goals = [k for (k,v) in collections.Counter(goals.values()).items() if v==1]
  no_move = [k for (k,v) in collections.Counter(goals.values()).items() if v>1]
  stay = [k for (k,v) in goals.items() if v in no_move]
  new_els += stay + pos_goals
  
  els = new_els
  pr(els)
  
  print(r+1,len(pos_goals))
  if len(pos_goals)==0:
    break