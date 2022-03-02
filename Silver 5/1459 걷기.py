a,b,c,d=map(int,input().split())
f,g=max(a,b),min(a,b)
z=f*d
if a%2-b%2:z+=c-d
print(min((a+b)*c,g*d+(f-g)*c,z))
