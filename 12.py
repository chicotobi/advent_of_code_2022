from scipy.sparse.csgraph import shortest_path

v = dict(zip(list('abcdefghijklmnopqrstuvwxyz'),range(1,27)))
v["S"] = 1
v["E"] = 26

d = [list(i) for i in open("12.txt").read().split("\n")[:-1]]
e = [[v[i] for i in j] for j in d]

n = len(d)
m = len(d[0])

def idx(i,j):
  return i*m+j

import numpy as np

a = np.zeros((n*m,n*m))

for (i,line) in enumerate(e):
  for (j,el) in enumerate(line):
    val = e[i][j]
    if i>0:
      if e[i-1][j] <= val+1:
        a[idx(i,j),idx(i-1,j)] = 1
    if i<n-1:
      if e[i+1][j] <= val+1:
        a[idx(i,j),idx(i+1,j)] = 1
    if j>0:
      if e[i][j-1] <= val+1:
        a[idx(i,j),idx(i,j-1)] = 1
    if j<m-1:
      if e[i][j+1] <= val+1:
        a[idx(i,j),idx(i,j+1)] = 1

r = shortest_path(a)

idx_s = [[idx(i,j) for (j,el) in enumerate(line) if el=='S'] for (i,line) in enumerate(d)]
idx_s = [i[0] for i in idx_s if len(i)>0][0]

idx_e = [[idx(i,j) for (j,el) in enumerate(line) if el=='E'] for (i,line) in enumerate(d)]
idx_e = [i[0] for i in idx_e if len(i)>0][0]

a = r[idx_s,:]

b = a.reshape((n,m))

print(r[idx_s,idx_e])
m = r[idx_s,idx_e]


idx_a = [[idx(i,j) for (j,el) in enumerate(line) if el=='a'] for (i,line) in enumerate(d)]
idx_a = [i[0] for i in idx_a if len(i)>0]

for a in idx_a:
  m = min(m,r[a,idx_e])
  print(r[a,idx_e])
print(m)


import matplotlib.pyplot as plt
import numpy as np

plt.imshow(b, cmap='hot', interpolation='nearest')
plt.show()