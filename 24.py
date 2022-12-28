d = open('24.txt', 'r').read().splitlines()

places = []
blizzards = []

nx = len(d)
ny = len(d[0])

for (i,line) in enumerate(d):
  for (j,el) in enumerate(line):
    if el in ['>','<','^','v']:
      places += [(i,j)]
      blizzards += [[i,j,el]]
    elif el == '.':
      places += [(i,j)]

loc = [(0,1)]
t = 0
stage = 0
while True:
  t += 1
  
  # Advance blizzards
  for b in blizzards:
    if b[2] == '>':
      b[1] = 1 if b[1] == ny-2 else b[1]+1
    if b[2] == 'v':
      b[0] = 1 if b[0] == nx-2 else b[0]+1
    if b[2] == '<':
      b[1] = ny-2 if b[1] == 1 else b[1]-1
    if b[2] == '^':
      b[0] = nx-2 if b[0] == 1 else b[0]-1
  
  blizzard_places = [(i,j) for (i,j,e) in blizzards]
  
  # Mark achievable places
  new_loc = []
  for (i,j) in loc:
   pos = [(i,j),(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
   pos = [(i,j) for (i,j) in pos if (i>0 and i<nx-1 and j>0 and j<ny-1) or (i==0 and j==1) or (i==nx-1 and j==ny-2)]
   pos = [p for p in pos if p not in blizzard_places]
   new_loc += pos 
  loc = list(set(new_loc))
  
  # Print
  print("t=",t)
  # for i in range(nx):
  #   s = ''
  #   for j in range(ny):
  #     if (i,j) not in places:
  #       s += '#'
  #     else:
  #       els = [el for (i0,j0,el) in blizzards if i==i0 and j==j0]
  #       if len(els)==0:
  #         if (i,j) in loc:
  #           s += 'E'
  #         else:
  #           s += '.'
  #       elif len(els)==1:
  #         s += els[0]
  #       else:
  #         s += str(len(els))
  #   print(s)
  # print()
  
  if stage==0 and (nx-1,ny-2) in loc:
    loc = [(nx-1,ny-2)]
    stage = 1
  if stage==1  and (0,1) in loc:
    loc = [(0,1)]
    stage = 2
  if stage==2 and (nx-1,ny-2) in loc:
    break        