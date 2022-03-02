a=input().split("-")
t=sum(map(int,a[0].split("+")))
for i in range(len(a)-1):t-=sum(map(int,a[i+1].split("+")))
print(t)
