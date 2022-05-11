a=int(input())
x=list(map(int,input().split()))
x.sort()
z=[]
for i in range(a):z.append(x[-i-1]+i)
print(max(z)+2)
