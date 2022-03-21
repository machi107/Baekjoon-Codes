x=[]
for i in range(8):x.append(int(input()))
t=x.copy()
x.sort()
r=[]
print(sum(x[3:]))
for i in range(5):
    r.append(t.index(x[i+3])+1)
r.sort()
print(r[0],r[1],r[2],r[3],r[4])
