d = open("4.txt", "r").read().splitlines()

d = [i.split(",") for i in d]
d = [i[0].split("-")+i[1].split("-") for i in d]
d = [[int(i) for i in j] for j in d]

c1 = [i for i in d if (i[0]>=i[2] and i[1]<=i[3]) or (i[0]<=i[2] and i[1]>=i[3])]
print(len(c1))


c1 = [i for i in d if i[1]<i[2] or i[3]<i[0]]
print(1000-len(c1))