d = open("6.txt", "r").read()

d = [i for i in d]
for i in range(len(d)):
  if len(set(d[i:i+4])) == 4:
    print(i+4)
    print(d[i:i+4])
    break

for i in range(len(d)):
  if len(set(d[i:i+14])) == 14:
    print(i+14)
    print(d[i:i+14])
    break