f = open("1.txt", "r")
sums = []
s = 0
for x in f.read().splitlines():
  if x == '':
    sums.append(s)
    s = 0
  else:
    s += int(x)
sums.sort()
print(sums[-1])
print(sum(sums[-3:]))