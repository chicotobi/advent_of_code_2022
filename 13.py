d = open("13.txt", "r").read().splitlines()

def compare(x,y):
  #print(x,y)
  if type(x) == int and type(y) == int:
    if x<y:
      return True
    if x>y:
      return False
    return None
  if type(y) == int:
    y = [y]
  if type(x) == int:
    x = [x]
  for i in range(min(len(x),len(y))):
    v = compare(x[i],y[i])
    if v is not None:
      return v
  if len(x) > len(y):
    return False
  elif len(y) > len(x):
    return True
  else:
    return None

s = 0
l = len(d)//3+1
for i in range(l):
  print()
  print("new")
  print()
  v1 = eval(d[3*i])
  v2 = eval(d[3*i+1])
  print(v1)
  print()
  print(v2)
  v = compare(v1,v2)
  if v is None:
    print("big mistake")
  elif v:
    print("right order")
    s += i+1
  else:
    print("not right order")
    s += 0
