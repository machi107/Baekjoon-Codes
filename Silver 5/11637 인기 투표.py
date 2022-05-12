p="winner"
q="ority"
for i in range(int(input())):
    x="min"
    r=[]
    for j in range(int(input())):r.append(int(input()))
    t=max(r)
    k=r.index(t)+1
    if sum(r)<t*2:x="maj"
    if r.count(t)>1:print("no",p)
    else:print(x+q,p,k)
