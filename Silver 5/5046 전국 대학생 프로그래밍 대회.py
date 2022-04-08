a,b,c,d=map(int,input().split())
z,e,f=b+1,[],[]
for i in range(c):e.append(int(input()));f.append(list(map(int,input().split())));f[i].sort()
for i in range(c):
    if a<=f[i][-1] and z>e[i]*a:z=e[i]*a
if z>b:print("stay home")
else:print(z)
