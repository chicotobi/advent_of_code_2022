d = open("11.txt", "r").read().split("\n")

n = 8
rounds = 10000

monkeys = []
for i in range(n):
  items = [int(i) for i in d[7*i+1][18:].split(",")]
  op = d[7*i+2][19:]
  div = int(d[7*i+3][21:])
  goals = [int(d[7*i+4][29:]), int(d[7*i+5][29:])]
  monkey = {"items":items, "op":op, "div":div, "goals":goals}
  monkeys.append(monkey)
  
from functools import reduce
divs = reduce(lambda x,y:x*y, [m["div"] for m in monkeys])

def do(monkey,old):
  new = eval(monkey["op"])
  new = new % divs
  if new%monkey["div"]==0:
    goal = monkey["goals"][0]
  else:
    goal = monkey["goals"][1]
  return goal, new

counter = {i:0 for i in range(n)}
for i in range(rounds):
  for j in range(n):
    for item in monkeys[j]["items"]:
      goal, item = do(monkeys[j],item)
      counter[j] += 1
      monkeys[goal]["items"] += [item]
    monkeys[j]["items"] = []
  #print("round",i)
  #print(monkeys)
  #print(counter)
print(counter)