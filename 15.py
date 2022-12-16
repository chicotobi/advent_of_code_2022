d = open("15.txt", "r").read().splitlines()

d = [i.split(" ") for i in d]
d = [[int(el.split("=")[1].replace(":","").replace(",","")) for (j,el) in enumerate(i) if j in [2,3,8,9]] for i in d]

beacons = set((i[2],i[3]) for i in d)

e = [[s[0],s[1],(abs(s[0]-s[2])+abs(s[1]-s[3]))] for s in d]

y = 2000000
#y = 10

xmin = min(min(s[0],s[2]) for s in d) - max(s[2] for s in e)
xmax = max(max(s[0],s[2]) for s in d) + max(s[2] for s in e)

# create exclusion intervals
excl_intv = []
for s in e:
  dist_x = s[2] - abs(y-s[1])
  if dist_x >= 0:
    excl_intv += [(s[0]-dist_x, s[0]+dist_x)]
excl_intv = sorted(excl_intv)

# simplify these intervals
v1 = excl_intv[0]
new_excl_intv = []
for i in range(1,len(excl_intv)-1):
  v2 = excl_intv[i]
  if v2[0] <= v1[1]:
    v1 = (min(v1[0],v2[0]), max(v1[1],v2[1]))
  else:
    new_excl_intv += [v1]
new_excl_intv += [v1]

lens = sum(i[1]-i[0] for i in new_excl_intv)
print(lens)

for y in range(4000000):
  xmin = 0
  xmax = 4000000

  y = 2906101

  if y%10000==0:
    print(y)

  # create exclusion intervals
  excl_intv = []
  for s in e:
    dist_x = s[2] - abs(y-s[1])
    if dist_x >= 0:
      excl_intv += [(max(0,s[0]-dist_x), min(xmax,s[0]+dist_x))]
  excl_intv = sorted(excl_intv)

  # simplify these intervals
  v1 = excl_intv[0]
  new_excl_intv = []
  for i in range(1,len(excl_intv)):
    v2 = excl_intv[i]
    if v2[0] <= v1[1]:
      v1 = (min(v1[0],v2[0]), max(v1[1],v2[1]))
    else:
      new_excl_intv += [v1]
    print(v1)
  new_excl_intv += [v1]
  if len(new_excl_intv) > 1:
    print(new_excl_intv,y)
    break