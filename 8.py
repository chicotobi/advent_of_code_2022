f = open("G:/Meine Ablage/code/8.txt").read().split("\n")

import numpy as np

f = [i for i in f if i!='']

n = len(f)

a = np.empty((n,n))

for (i,row) in enumerate(f):
  for (j,el) in enumerate(row):
    a[i,j] = int(el)

# visibility matrix
visible = np.zeros((n,n))

# left
for i in range(n):
  height = -1
  for j in range(n):
    if a[i,j]> height:
      visible[i,j] = 1
      height = a[i,j]

# top
for i in range(n):
  height = -1
  for j in range(n):
    if a[j,i]> height:
      visible[j,i] = 1
      height = a[j,i]

# right
for i in range(n):
  height = -1
  for j in range(n):
    if a[i,n-1-j]> height:
      visible[i,n-1-j] = 1
      height = a[i,n-1-j]

# bottom
for i in range(n):
  height = -1
  for j in range(n):
    if a[n-1-j,i]> height:
      visible[n-1-j,i] = 1
      height = a[n-1-j,i]

print(int(np.sum(visible)))

scenic_score = np.zeros((n,n))
for i in range(n):
  for j in range(n):
    score = 1
    height = a[i,j]

    # to the right
    k = 1
    for k in range(1,n-j):
      if a[i,j+k] >= height:
        break
    score *= k

    # to the left
    k = 1
    for k in range(1,j+1):
      if a[i,j-k] >= height:
        break
    score *= k

    # to the bottom
    k = 1
    for k in range(1,n-i):
      if a[i+k,j] >= height:
        break
    score *= k

    # to the top
    k = 1
    for k in range(1,i+1):
      if a[i-k,j] >= height:
        break
    score *= k

    scenic_score[i,j] = score

print(int(np.max(scenic_score)))

























