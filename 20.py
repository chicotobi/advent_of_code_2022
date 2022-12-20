number = open("20.txt", "r").read().splitlines()
number = [int(i) for i in number]

n = len(number)
order = list(range(n))
new_order = list(range(n))

for i in order:
  if i%100==0:
    print(i)
  num0 = number[i]
  pos = new_order[i]
  num = (num0+pos)%(n-1) - pos
  if num == 0:
    continue
  elif 0 < num:
      change_pos = range(pos+1,pos+num+1)
      val1 = num
      val2 = -1
  elif num < 0:
      change_pos = range(pos+num,pos+1)
      val1 = num
      val2 = 1
  for j in range(n):
    if order[j] == i:
      new_order[j] += val1
    elif new_order[j]  in change_pos:
      new_order[j] += val2
print(number,order,new_order)

idx = [new_order0 for(number0,new_order0) in zip(number,new_order) if number0 == 0][0]
val1 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+1000][0]
val2 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+2000][0]
val3 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+3000][0]
print(val1+val2+val3)

# part 2
number = open("20.txt", "r").read().splitlines()
number = [int(i) for i in number]
n = len(number)
order = list(range(n))
new_order = list(range(n))
number = [i*811589153 for i in number]

for k in range(10):
  for i in order:
    if i%100==0:
      print(k,i)
    num0 = number[i]
    pos = new_order[i]
    num = (num0+pos)%(n-1) - pos
    if num == 0:
      continue
    elif 0 < num:
        change_pos = range(pos+1,pos+num+1)
        val1 = num
        val2 = -1
    elif num < 0:
        change_pos = range(pos+num,pos+1)
        val1 = num
        val2 = 1
    for j in range(n):
      if order[j] == i:
        new_order[j] += val1
      elif new_order[j]  in change_pos:
        new_order[j] += val2
print(number,order,new_order)

idx = [new_order0 for(number0,new_order0) in zip(number,new_order) if number0 == 0][0]
val1 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+1000][0]
val2 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+2000][0]
val3 = [number0 for(number0,new_order0) in zip(number,new_order) if new_order0 == idx+3000][0]
print(val1+val2+val3)