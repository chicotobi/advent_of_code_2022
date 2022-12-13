d = open("10.txt", "r").read().split("\n")[:-1]

def f(cycle,r,v,x,s):
  print(cycle,r)
  if cycle in [20,60,100,140,180,220]:
    s += x*cycle 
    print("signal strength calc ",x*cycle,s)
  return s

screen = []
line = []
s = 0
cycle = 0
v = 0
x = 1
for r in d:
  if r == 'noop':
    if abs(x-cycle)<=1:
      line += ['#']
    else:
      line += ['.']
    if(len(line)==40):
      screen += [line]
      cycle -= 40
      line = []
    cycle += 1
    s = f(cycle,r,v,x,s)
  else:
    if abs(x-cycle)<=1:
      line += ['#']
    else:
      line += ['.']
    if(len(line)==40):
      screen += [line]
      cycle -= 40
      line = []
    cycle += 1
    s = f(cycle,r,v,x,s)
    if abs(x-cycle)<=1:
      line += ['#']
    else:
      line += ['.']
    if(len(line)==40):
      screen += [line]
      cycle -= 40
      line = []
    cycle += 1
    s = f(cycle,r,v,x,s)
    v = int(r[4:])
    x += v
print(s)

print([''.join(line) for line in screen])