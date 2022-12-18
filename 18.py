d = open("18.txt", "r").read().splitlines()
d = [i.split(",") for i in d]
d = [[int(j) for j in i] for i in d]


xmin = min(i[0] for i in d)
ymin = min(i[1] for i in d)
zmin = min(i[2] for i in d)
xmax = max(i[0] for i in d)
ymax = max(i[1] for i in d)
zmax = max(i[2] for i in d)

d2 = [[xmax+1,ymax+1,zmax+1]]
for i in d2:
  x = i[0]
  y = i[1]
  z = i[2]
  n = len(d2)
  
  x0 = min(max(x+1,xmin-1),xmax+1)
  el = [x0,y,z]
  if el not in d2 and el not in d:
    d2 += [el]
  
  x0 = min(max(x-1,ymin-1),ymax+1)
  el = [x0,y,z]
  if el not in d2 and el not in d:
    d2 += [el]
    
  y0 = min(max(y+1,ymin-1),ymax+1)
  el = [x,y0,z]
  if el not in d2 and el not in d:
    d2 += [el]
  
  y0 = min(max(y-1,ymin-1),ymax+1)
  el = [x,y0,z]
  if el not in d2 and el not in d:
    d2 += [el]
    
  z0 = min(max(z+1,zmin-1),zmax+1)
  el = [x,y,z0]
  if el not in d2 and el not in d:
    d2 += [el]
  
  z0 = min(max(z-1,zmin-1),zmax+1)
  el = [x,y,z0]
  if el not in d2 and el not in d:
    d2 += [el]
    
n = 0
for i in d:
  x = i[0]
  y = i[1]
  z = i[2]
  if [x+1,y,z] in d2:
    n += 1
  if [x-1,y,z] in d2:
    n += 1
  if [x,y+1,z] in d2:
    n += 1
  if [x,y-1,z] in d2:
    n += 1
  if [x,y,z+1] in d2:
    n += 1
  if [x,y,z-1] in d2:
    n += 1
print(n)

