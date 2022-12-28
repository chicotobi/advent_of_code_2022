d = open("25.txt").read().splitlines()

def snafu(x):
  y = 0
  for i in x:
    y *= 5
    if i == '2':
      y += 2
    elif i == '1':
      y += 1
    elif i == '-':
      y -= 1
    elif i == '=':
      y -= 2    
  return y

def dec(x):
  s = []
  n = 1
  incr = 0
  while x>4:
    z = x % 5
    x = x // 5
    if z+incr in [0,1,2]:
      s += [z+incr]
      incr = 0
    else:
      s += [z+incr-5]
      incr = 1
    n += 1
  if x+incr in [0,1,2]:
    s += [x+incr]
    incr = 0
  else:
    s += [x+incr-5]
    incr = 1  
  s2 = []
  for i in s:
    if i == -1:
      s2 += '-'
    elif i == -2:
      s2 += '='
    else:
      s2 += str(i)
  return ''.join(s2[::-1])

print(dec(sum(snafu(x) for x in d)))