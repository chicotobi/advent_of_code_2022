from functools import cache

d = open("19.txt", "r").read().splitlines()
d = [i.split(" ") for i in d]
d = [(i[6],i[12],i[18],i[21],i[27],i[30]) for i in d]
d = [list(int(j) for j in i) for i in d]
d = [((i[0],0,0),(i[1],0,0),(i[2],i[3],0),(i[4],0,i[5])) for i in d]

@cache
def get_value(blp,robots,goods,steps):
  robots0 = robots
  goods0 = goods
  steps0 = steps

  if steps>20:
    print(robots,goods,steps)

  max_val = goods[3]
  max_orders = []
  for next_robot in range(4):
    robots = robots0
    goods = goods0
    steps = steps0

    cst = blp[next_robot]
    new_robot = False
    while not new_robot and steps>0:
      steps -= 1

      # order
      if cst[0] <= goods[0] and cst[1] <= goods[1] and cst[2] <= goods[2]:
        new_robot = True
        goods = (goods[0]-cst[0],goods[1]-cst[1],goods[2]-cst[2],goods[3])

      # produce
      goods = (goods[0]+robots[0],goods[1]+robots[1],goods[2]+robots[2],goods[3]+robots[3])

      # Prune the tree - if we have already more goods than we can ever use for building
      max_needed_goods = [max(r[j] for r in blp)*steps for j in range(3)]
      g0 = min(goods[0],max_needed_goods[0])
      g1 = min(goods[1],max_needed_goods[1])
      g2 = min(goods[2],max_needed_goods[2])
      goods = (g0,g1,g2,goods[3])

    if steps==0:
      val = goods[3]
      orders = [-1]
    else:
      robots = list(robots)
      robots[next_robot] +=1
      robots = tuple(robots)
      val, orders = get_value(blp,robots,goods,steps)
      orders = [next_robot] + orders

    if val > max_val:
      max_val = val
      max_orders = orders

  return max_val, max_orders

# Part 1
# vals = []
# orders = []
# s = 0
# for (i,blp) in enumerate(d):
#   print(i+1,"of",len(d),blp)
#   steps = 24
#   robots = (1,0,0,0)
#   goods = (0,0,0,0)
#   val, order = get_value(blp,robots,goods,steps)
#   vals += [val]
#   orders += [order]
#   s += val*(i+1)
#   print(get_value.cache_info())
# print(s)


# Part 2
robots = (1,0,0,0)
goods = (0,0,0,0)
steps = 32
val1, orders1 = get_value(d[0],robots,goods,32)
val2, orders2 = get_value(d[1],robots,goods,32)
val3, orders3 = get_value(d[2],robots,goods,32)
print(val1*val2*val3)
