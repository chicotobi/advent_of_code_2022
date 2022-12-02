s = 0
for line in open("2.txt", "r").read().splitlines():
  if "X" in line:
    s += 1
  if "Y" in line:
    s += 2
  if "Z" in line:
    s += 3
  if line in ["A X", "B Y", "C Z"]:
    s += 3
  if line in ["A Y", "B Z", "C X"]:
    s += 6
  if line in ["A Z", "B X", "C Y"]:
    s += 0
print(s)

s = 0
for line in open("2.txt", "r").read().splitlines():
  if "X" in line:
    s += 0
  if "Y" in line:
    s += 3
  if "Z" in line:
    s += 6
  if line in ["A Y", "B X", "C Z"]:
    s += 1
  if line in ["A Z", "B Y", "C X"]:
    s += 2
  if line in ["A X", "B Z", "C Y"]:
    s += 3
print(s)