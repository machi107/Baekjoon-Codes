a,b=input().split()
t=0
for i in range(1,int(a)+1):t+=str(i).count(b)
print(t)
