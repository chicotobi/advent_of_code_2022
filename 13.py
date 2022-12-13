d = open("13.txt", "r").read().splitlines()

def compare(x,y):
  if type(x) == int and type(y) == int:
    if x < y:
      return -1
    elif x > y:
      return 1
    else:
      return 0
  if type(y) == int:
    y = [y]
  if type(x) == int:
    x = [x]
  for i in range(min(len(x),len(y))):
    v = compare(x[i],y[i])
    if v != 0:
      return v
  if len(x) < len(y):
    return -1
  elif len(x) > len(y):
    return 1
  else:
    return 0

s = 0
l = len(d)//3+1
for i in range(l):
  v1 = eval(d[3*i])
  v2 = eval(d[3*i+1])
  v = compare(v1,v2)
  if v == -1:
    s += i+1
print(s)

d2 = [eval(i) for i in d if i!=""] + [[[2]],[[6]]]

import functools

list.sort(d2, key=functools.cmp_to_key(compare))

idx1 = [i for (i,v) in enumerate(d2) if v==[[2]]][0] + 1
idx2 = [i for (i,v) in enumerate(d2) if v==[[6]]][0] + 1
print(idx1*idx2)