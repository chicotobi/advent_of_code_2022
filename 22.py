d = open("22.txt", "r").read().splitlines()

a = {}
i = 0
while d[i]!="":
  tmp = [j for j in d[i]]
  for j in range(len(tmp)):
    if tmp[j] == '.':
      a[(i,j)] = 0
    elif tmp[j] == '#':
      a[(i,j)] = 1
  i += 1

path = d[i+1].replace("R"," R ").replace("L"," L ").split(" ")

trans = {}
for el in a:
  i = el[0]
  j = el[1]
  if a[el]==1:
    continue

  # First find the partner
  if (i,j+1) in a:
    j_r = j+1
  else:
    j_r = min(j0 for (i0,j0) in a.keys() if i0==i)
  el_r = (i,j_r)

  # Now check the type
  if a[el_r] == 0:
    trans[(i,j,0)] = el_r
  else:
    trans[(i,j,0)] = el

  # First find the partner
  if (i,j-1) in a:
    j_l = j-1
  else:
    j_l = max(j0 for (i0,j0) in a.keys() if i0==i)
  el_l = (i,j_l)

  # Now check the type
  if a[el_l] == 0:
    trans[(i,j,2)] = el_l
  else:
    trans[(i,j,2)] = el

  # First find the partner
  if (i+1,j) in a:
    i_d = i+1
  else:
    i_d = min(i0 for (i0,j0) in a.keys() if j0==j)
  el_d = (i_d,j)

  # Now check the type
  if a[el_d] == 0:
    trans[(i,j,1)] = el_d
  else:
    trans[(i,j,1)] = el

  # First find the partner
  if (i-1,j) in a:
    i_u = i-1
  else:
    i_u = max(i0 for (i0,j0) in a.keys() if j0==j)
  el_u = (i_u,j)

  # Now check the type
  if a[el_u] == 0:
    trans[(i,j,3)] = el_u
  else:
    trans[(i,j,3)] = el


i = 0
j = min(j for (i,j) in a.keys() if i == 0)
o = 0
print(i,j,o)

for el in path:
  if el=="R":
    o = (o+1)%4
    #print(i,j,o)
  elif el=="L":
    o = (o-1)%4
    #print(i,j,o)
  else:
    way = int(el)
    for k in range(way):
      i, j = trans[(i,j,o)]
      #print(i,j,o)
print(1000*(i+1)+4*(j+1)+o)