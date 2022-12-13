d = open("13.txt", "r").read().splitlines()

def compare(x,y):
  #print(x,y)
  if type(x) == int and type(y) == int:
    if x<y:
      return True
    if x>y:
      return False
    return None
  if type(x) == list and type(y) == int:
    return compare(x,[y])
  if type(x) == int and type(y) == list:
    return compare([x],y)
  for i in range(len(x)):
    if len(y) < i + 1:
      return False
    v = compare(x[i],y[i])
    if v is not None:
      return v
  return True

s = 0
l = len(d)//3+1
for i in range(l):
  #print()
  #print()
  v1 = eval(d[3*i])
  v2 = eval(d[3*i+1])
  v = compare(v1,v2)
  if v is None:
    print("big mistake")
  elif v:
    #print("right order")
    s += i+1
  else:
    #print("not right order")
    s += 0
