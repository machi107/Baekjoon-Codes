a=int(input())
for i in range(a):
    x=[]
    r=0
    for j in range(3):
        x.append(list(map(int,input().split())))
    if x[0][0]-x[0][1]==x[0][1]-x[0][2]:r+=1
    if x[2][0]-x[2][1]==x[2][1]-x[2][2]:r+=1
    if x[0][0]-x[1][0]==x[1][0]-x[2][0]:r+=1
    if x[0][2]-x[1][1]==x[1][1]-x[2][2]:r+=1
    t=[x[1][1]+x[1][0],x[0][1]+x[2][1],x[0][0]+x[2][2],x[2][0]+x[0][2]]
    z=[]
    for j in range(4):
        if t[j]/2%1==0:z.append(t[j])
    if len(z):r=r+len(z)+1-len(set(z))
    print("Case #{0}: {1}".format(i+1,r))
