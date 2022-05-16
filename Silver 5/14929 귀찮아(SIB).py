a=int(input())
t=list(map(int,input().split()))
q=sum(t)
r=0
for i in range(a):r+=(q-t[i])*t[i]
print(r//2)
