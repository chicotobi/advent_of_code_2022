from scipy.sparse.csgraph import shortest_path
import numpy as np

d = open("16.txt").read().split("\n")

n = len(d)

a = np.zeros((n,n))

idx = {j.split(" ")[1]:i  for (i,j) in enumerate(d)}
arr_pressure = []

for (idx0,j) in enumerate(d):
  val = int(j.split(" ")[4].split("=")[1].replace(";",""))
  arr_pressure.append(val)
  for k in j.split(" ")[9:]:
    idx1 = idx[k.replace(",","")]
    a[idx0,idx1] = 1

r = shortest_path(a)

t = 30
t1 = 26
loc0 = idx["AA"]
closed_valves = tuple(i for (i,j) in enumerate(arr_pressure) if j>0)

import functools
@functools.lru_cache(maxsize=None)
def val_elefant(loc,closed_valves,t,current_release):
  best_release, best_order = val_alone(loc0, closed_valves, t1, 0)
  for valve in closed_valves:
    if(len(closed_valves)>13):
      print(" "*(15-len(closed_valves)),"elefant open",valve)
    cv = set(closed_valves)
    cv.remove(valve)
    cv = tuple(cv)
    dist = r[loc,valve]
    if t-dist-1 >= 0:
      new_release = current_release + arr_pressure[valve]
      release, order = val_elefant(valve,cv,t-dist-1,new_release)
      release += current_release * (dist+1)
      if best_release < release:
        best_release = release
        best_order = [valve] + order
  return best_release, best_order

@functools.lru_cache(maxsize=None)
def val_alone(loc,closed_valves,t,current_release):
  best_release = t * current_release
  best_order = []
  for valve in closed_valves:
    cv = set(closed_valves)
    cv.remove(valve)
    cv = tuple(cv)
    dist = r[loc,valve]
    if t-dist-1 >= 0:
      new_release = current_release + arr_pressure[valve]
      release, order = val_alone(valve,cv,t-dist-1,new_release)
      release += current_release * (dist+1)
      if best_release < release:
        best_release = release
        best_order = [valve] + order
  return best_release, best_order

release, order = val_alone(loc0,closed_valves,30,0)
print(release)
print(order)

release, order = val_elefant(loc0,closed_valves,t1,0)
print(release)
print(order)