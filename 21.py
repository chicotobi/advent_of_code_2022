d = open("21.txt", "r").read().splitlines()
d = sorted(d, key=len)
d = [i.replace(":","=") for i in d]

# while True:
#   n = 0
#   for i in d:
#     try:
#       exec(i)
#     except:
#       n+= 1
#   if n==0:
#     break

# print(root)

d1 = [i                  for i in d if "root" not in i and "humn=" not in i]
d2 = [i.replace("+","-") for i in d if "root" in i]

d = d1 + d2

a = 1000000000000
b = 10000000000000
while True:
  humn = round((a+b)/2)
  ldict = {}
  while True:
    n = 0
    exec("humn="+str(humn),globals(),ldict)
    for i in d:
      try:
        exec(i,globals(),ldict)
      except:
        n+= 1
    if n==0:
      root = ldict['root']
      break
  print(a,b,humn,root)
  if root>0:
    a = humn
  elif root<0:
    b = humn
  else:
    print(humn)
    break