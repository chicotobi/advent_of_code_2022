from numpy import sign

def add(pos,s):
  x = pos[0]
  y = pos[1]
  if s=="L":
    return (x-1,y)
  elif s=="R":
    return (x+1,y)
  elif s=="U":
    return (x,y+1)
  elif s=="D":
    return (x,y-1)

def pull(lead,lag):
  distance = (lead[0]-lag[0], lead[1]-lag[1])
  if max(abs(i) for i in distance)==2:
    return (lag[0] + sign(distance[0]), lag[1] + sign(distance[1]))
  else:
    return lag

steps = [i.split() for i in open("9.txt").read().split("\n")]

def tail_pos(length):
  rope = [(0,0)] * length

  tail_pos = [rope[-1]]
  for (direction,n) in steps:
    for j in range(int(n)):
      # Move head
      rope[0] = add(rope[0],direction)

      # Move rest
      for k in range(length-1):
        rope[k+1] = pull(rope[k],rope[k+1])

      tail_pos.append(rope[-1])
  print(len(set(tail_pos)))

tail_pos(2)
tail_pos(10)