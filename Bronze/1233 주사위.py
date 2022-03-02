a,b,c=map(int,input().split())
x,t=a+b+c+3,max(a,b,c)
if t+t>=x-3:x+=x-t-t-4
print(x//2)
