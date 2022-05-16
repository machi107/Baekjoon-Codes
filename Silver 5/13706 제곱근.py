k=input()
t=int(k)
z=("1"+"0"*((len(k)-1)//2))
z=int(z)
p=z*10
q=(z+p)//2
while(q**2!=t):
    if q**2<t:z=q
    else:p=q
    q=(z+p)//2
print(q)
