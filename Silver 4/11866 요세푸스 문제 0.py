a,b=map(int,input().split())
x=list(range(1,a+1))
t=0
z="<"
while(len(x)):
    t+=b-1
    while (t>=len(x)):t-=len(x)
    z+=str(x[t])+", "
    del x[t]
print(z[:-2]+">")
