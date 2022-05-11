a=int(input())
q=a-1
z=a-2
p=2*a
for i in range(p-1):
    r=1
    if i==a-1:r=0
    if i==0 or i==q*2:print("*"*a+" "*(q*2-1)+"*"*a)
    else:print(" "*min(i,q*2-i)+"*"+" "*z+"*"+" "*(max(i-q,q-i)*2-1)+"*"*r+" "*z+"*")
