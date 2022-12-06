from functools import reduce

d = open("5.txt", "r").read().splitlines()

initial = d[:8]
initial = [[j[i] for i in range(1,35,4)] for j in initial]

a = [[]]*len(initial[0])
for height in initial:
  for (j,element) in enumerate(height):
    if element != ' ':
      a[j] = [element] + a[j]

moves = [i.split() for i in d[10:]]

for m in moves:
  n = int(m[1])
  start = int(m[3]) - 1 
  end = int(m[5]) - 1
  for i in range(n):
    v = a[start].pop()
    a[end].append(v)
    
answer = [i[-1] for i in a]
answer = ''.join(answer)
print(answer)


d = open("5.txt", "r").read().splitlines()

initial = d[:8]
initial = [[j[i] for i in range(1,35,4)] for j in initial]

a = [[]]*len(initial[0])
for height in initial:
  for (j,element) in enumerate(height):
    if element != ' ':
      a[j] = [element] + a[j]

moves = [i.split() for i in d[10:]]

for m in moves:
  n = int(m[1])
  start = int(m[3]) - 1 
  end = int(m[5]) - 1
  v = []
  for i in range(n):
    v = [a[start].pop()] + v
  for i in v:
    a[end].append(i)
    
answer = [i[-1] for i in a]
answer = ''.join(answer)
print(answer)
