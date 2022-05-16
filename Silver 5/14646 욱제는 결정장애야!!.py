x=[0 for i in range(int(input()))]
t=list(map(int,input().split()))
z=[]
p=0
for i in range(len(t)):
    x[t[i]-1]+=1
    if x[t[i]-1]%2:p+=1
    else:p-=1
    z.append(p)
print(max(z))
