d = open("22.txt", "r").read().splitlines()
n = 50

a = {}
i = 0
while d[i]!="":
  tmp = [j for j in d[i]]
  for j in range(len(tmp)):
    if tmp[j] == '.':
      a[(i+1,j+1)] = 0
    elif tmp[j] == '#':
      a[(i+1,j+1)] = 1
  i += 1

path = d[i+1].replace("R"," R ").replace("L"," L ").split(" ")

trans = {}
for el in a:
  i = el[0]
  j = el[1]

  # First add direct partner
  if (i,j+1) in a:
      trans[(i,j,0)] = (i,j+1,0)
  if (i,j-1) in a:
      trans[(i,j,2)] = (i,j-1,2)
  if (i+1,j) in a:
      trans[(i,j,1)] = (i+1,j,1)
  if (i-1,j) in a:
      trans[(i,j,3)] = (i-1,j,3)

for i in range(1,n+1):
  trans[(1,50+i,3)] = (150+i,1,0)  
  trans[(150+i,1,2)] = (1,50+i,1)

  trans[(1,100+i,3)] = (200,i,3)
  trans[(200,i,1)] = (1,100+i,1)

  trans[(i,150,0)] = (151-i,100,2)
  trans[(151-i,100,0)] = (i,150,2)

  trans[(50,151-i,1)] = (101-i,100,2)
  trans[(101-i,100,0)] = (50,151-i,3)

  trans[(150,50+i,1)] = (150+i,50,2)
  trans[(150+i,50,0)] = (150,50+i,3)

  trans[(i,51,2)] = (151-i,1,0)
  trans[(151-i,1,2)] = (i,51,0)

  trans[(50+i,51,2)] = (101,i,1)
  trans[(101,i,3)] = (50+i,51,0)
  
for k in a.keys():
  for o in range(4):
    i,j,o0 = trans[k+(o,)]
    if a[i,j] == 1:
      trans[k+(o,)] = k+(o,)
    
i = 1
j = min(j for (i,j) in a.keys() if i == 1)
o = 0

walk = []
for el in path:
  if el=="R":
    o = (o+1)%4
  elif el=="L":
    o = (o-1)%4
  else:
    way = int(el)
    for k in range(way):
      i, j, o = trans[(i,j,o)]
print(1000*(i)+4*(j)+o)