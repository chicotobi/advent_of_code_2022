d = open("14.txt", "r").read().splitlines()
d = [i.split(" -> ") for i in d]
d = [[j.split(",") for j in i] for i in d]
d = [[[int(k) for k in j] for j in i] for i in d]

# For Part two
#d += [[[462-173,173],[534+173,173]]]

minx = min(min(j[0] for j in i) for i in d)
maxx = max(max(j[0] for j in i) for i in d)
maxy = max(max(j[1] for j in i) for i in d)

w = maxx - minx + 1
h = maxy + 1
a = [['.']*w for i in range(h)]

d = [[[j[0]-minx,j[1]] for j in i] for i in d]


def myrange(a,b):
  if a<b:
    return list(range(a,b+1))
  else:
    return list(range(b,a+1))

def pr(a):
  print('\n'.join(''.join(i) for i in a))
  print()

for line in d:
  for i in range(len(line)-1):
    vertex1 = line[i]
    vertex2 = line[i+1]
    #print(vertex1,vertex2)
    if vertex1[0] == vertex2[0]:
      for j in myrange(vertex1[1],vertex2[1]):
        #print(vertex1[0],j)
        a[j][vertex1[0]] = '#'
        #pr(a)
    else:
      for j in myrange(vertex1[0],vertex2[0]):
        #print(j,vertex1[1])
        a[vertex1[1]][j] = '#'
        #pr(a)

ns = 0
while True:
  sx = 500 - minx
  sy = 0

  #pr(a)
  #input()

  # New sand
  if a[sy][sx] == '.':
    a[sy][sx] = 'o'
  else:
    break

  stop = False

  # Falling
  while True:
    if sy == h - 1:
      a[sy][sx] = '.'
      stop = True
      break
    elif a[sy+1][sx] == '.':
      a[sy][sx] = '.'
      sy += 1
      a[sy][sx] = 'o'
    else:
      if sx == 0:
        a[sy][sx] = '.'
        stop = True
        break
      elif a[sy+1][sx-1] == '.':
        a[sy][sx] = '.'
        sy += 1
        sx -= 1
        a[sy][sx] = 'o'
      else:
        if sx == w-2:
          a[sy][sx] = '.'
          stop = True
          break
        elif a[sy+1][sx+1] == '.':
          a[sy][sx] = '.'
          sy += 1
          sx += 1
          a[sy][sx] = 'o'
        else:
          break
  if stop:
    break
  ns += 1
print(ns)

from PIL import Image
import numpy as np

foo = np.zeros([h,w,3], dtype=np.int8)
for i in range(h):
  for j in range(w):
    if a[i][j] == '#':
      foo[i,j] = [255,255,255]
    elif a[i][j] == 'o':
      foo[i,j] = [255,255,0]
img = Image.fromarray(foo, 'RGB')
img.save('out.png')