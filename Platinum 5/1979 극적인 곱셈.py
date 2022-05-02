a,b=map(int,input().split())
x=0
for i in range(100):
    b+=int(str(b)[-i-1])*a*(10**(i+1))
    k=str(b)
    if k[0]==k[-1] and k[1]!="0" and int(k[1:])*a==int(k[:-1]):x=int(k[1:]);break
print(x)
