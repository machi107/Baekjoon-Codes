a,x=int(input()),[]
for i in range(a):t=(list(map(int,input().split())));k=sum(t)-t[0];r=t[1]*t[2]*t[3];x.append([r,k,t[0]])
x.sort()
print(x[0][2],x[1][2],x[2][2])
