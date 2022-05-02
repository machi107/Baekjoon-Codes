a=int(input())
t=0
if a==1:t=3
for i in range(2,int(a**0.5)+1):
    if a%i==0:t+=1;a=a/i
for i in range(2,int(a**0.5)+1):
    if a%i==0:t+=1;break
if t!=1:print("koosaga")
else: print("cubelover")
