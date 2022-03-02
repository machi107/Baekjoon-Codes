a,b=map(int,input().split())
if a<=b:
 for i in range(1,a+1):
  if (a/i)**i>=b:print(i);break
 if i==a:print(-1)
else:print(2)
