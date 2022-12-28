import copy

d = open('17.txt').read().replace("\n","")
d = [i for i in d]
n_jet = len(d)

p1 = [[0,2],[0,3],[0,4],[0,5]]
p2 = [[0,3],[1,2],[1,3],[1,4],[2,3]]
p3 = [[0,2],[0,3],[0,4],[1,4],[2,4]]
p4 = [[0,2],[1,2],[2,2],[3,2]]
p5 = [[0,2],[0,3],[1,2],[1,3]]
pieces = [p1,p2,p3,p4,p5]

n = 7
hmax = 1_000_000
field = []
for i in range(hmax):
    field += [['.']*7]

h0 = 0

def get_height(h0, field):
    for i in range(max(0,h0-3),hmax):
        filled = False
        for j in range(n):
            if field[i][j] == '#':
                filled = True
        if not filled:
            break
    return i
   
def init_piece(field,idx,h0):
    p = pieces[idx]
    h = get_height(h0,field) + 3
    return p, h

def shift(field,piece,h,idx_jet):
    dr = d[idx_jet]
    possible = True
    pnew = []
    if dr == ">":
        if max(x[1] for x in piece) == n-1:
            return piece
        for x in piece:
            pnew += [[x[0],x[1]+1]]
            if field[x[0]+h][x[1]+1] == '#':
                possible  = False
    else:
        if min(x[1] for x in piece) == 0:
            return piece
        for x in piece:
            pnew += [[x[0],x[1]-1]]
            if field[x[0]+h][x[1]-1] == '#':
                possible  = False
    if possible:
        return pnew
    else:
        return piece

def fall(field,piece, h):
    falling = True
    for x in piece:
        if x[0]+h-1 < 0:
            falling = False
        elif field[x[0]+h-1][x[1]] == '#':
            falling = False
    if falling:
        return True, field, h-1
    for x in piece:
        field[x[0]+h][x[1]] = '#'
    return False, field, -1

def pr(field,piece,h):
    i0 = max(0,h-20)
    i1 = h+5
    f2 = copy.deepcopy(field[i0:i1])
    #for x in piece:
    #    f2[x[0]+h][x[1]] = '@'
    tmp = [''.join(i) for i in f2]
    tmp = list(reversed(tmp))
    print('\n'.join(tmp))
    input("next?")

idx = 0
idx_jet = 0
i = 0
last_val = 0
i_max = 4500
data = []

h0 = 0
arr = []
tmp = get_height(h0,field)

while i < i_max:
    # Initialize piece
    piece, h = init_piece(field,idx,h0)
    h0 = h - 3
    idx = (idx+1)%5
    
    # Let it fall
    falling = True
    while falling:
        piece = shift(field,piece,h,idx_jet)
        idx_jet = (idx_jet+1)%n_jet
       
        falling, field, h = fall(field, piece, h)
    i += 1
    data += [(idx,idx_jet,h0)]
        
    if i%(349*5)==312:
      print(i)
      tmp1 = get_height(h0,field)
      arr += [tmp1-tmp]
      tmp = tmp1
   
print(get_height(h0,field))