import string
d = open("3.txt", "r").read().splitlines()

d2 = [set(a[:len(a)//2]).intersection(set(a[len(a)//2:])) for a in d]

val = dict(zip(string.ascii_letters, range(1,53)))

d3 = [val[list(a)[0]] for a in d2]

print(sum(d3))

import string
d = open("3b.txt", "r").read().splitlines()

s = 0
for i in range(100):
    s1 = set(d[3*i+0])
    s2 = set(d[3*i+1])
    s3 = set(d[3*i+2])
    res = s1.intersection(s2).intersection(s3)
    s += val[list(res)[0]]
print(s)