a=int(input())
x=[]
for i in range(a):b,c,d=map(int,input().split());x.append([d,b,c])
x.sort(reverse=True)
g=x[0][1:]
s=x[1][1:]
t=2
if g[0]==s[0]:
    for i in range(a):
        if x[i][1]!=g[0]:t=i;break
b=x[t][1:]
print(g[0],g[1])
print(s[0],s[1])
print(b[0],b[1])
