f = open("C:/Users/hofmant3/Downloads/7.txt").read().split("\n")

import pandas as pd

df = pd.DataFrame({"idx":[0],"frm":[-1],"name":[""],"sz":[0],"typ":["dir"]})

next_idx = 1
ptr = [0]
for i in f:
  if i in ["$ cd /", "$ ls", ""]:
    continue
  elif i == "$ cd ..":
    ptr.pop()
    continue
  elif i[:4] == "$ cd":
    idx_folder = df[(df.frm==ptr[-1])&(df.name==i[5:])].idx[0]
    ptr.append(idx_folder)
    continue
  elif i[:3] == "dir":
    tmp = pd.DataFrame({"idx":next_idx,"frm":ptr[-1],"name":i[4:],"typ":"dir","sz":0}, index=[0])
    df = pd.concat([df,tmp])
    next_idx +=1
  else:
    sz, name = i.split()
    tmp = pd.DataFrame({"idx":next_idx,"frm":ptr[-1],"name":name,"typ":"file","sz":int(sz)}, index=[0])
    df = pd.concat([df,tmp])
    next_idx +=1


def find_dir_size(idx):
  for i in df[(df.frm==idx)&(df.sz==0)].idx.values:
    find_dir_size(i)
  sz = sum(df[df.frm==idx].sz.values)
  df.loc[df.idx==idx,"sz"] = sz

find_dir_size(0)

final = sum(df[(df.typ=="dir")&(df.sz<=100000)].sz.values)
print(final)

unused = 70000000 - df[df.idx==0].sz.values
needed = 30000000 - unused
print(df[(df.typ=="dir")&(df.sz>=needed[0])].sz.values.min())