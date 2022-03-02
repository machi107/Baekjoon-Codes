a=list(input())
a.sort()
t=len(a)//2
x=""
for i in a:x+=i
z=x[::2]
q=x[1::2]
if len(a)%2:
    for r in range(t):
        if z[r]!=q[r]:z=z[:r]+z[r+1:]+z[r];break
print(z+q[::-1]) if z[:t]==q else print("I'm Sorry Hansoo")
