import sys
in_put = sys.stdin.readline

a=int(in_put())
ans=[0 for _ in range(20000001)]
x=list(map(int,in_put().split()))
for i in range(a):
    ans[x[i]+10000000]+=1
    

b= int(in_put())
y=list(map(int,in_put().split()))
for i in range(b):
    print(ans[y[i]+10000000],end=" ")
    
    
