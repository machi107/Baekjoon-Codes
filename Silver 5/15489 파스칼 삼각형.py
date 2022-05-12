a,b,c=map(int,input().split())
z=0
s=[[0 for _ in range(a+c)] for _ in range(a+c)]
s[0][0]=1
for i in range(a+c):
    for j in range(a+c-i):
        if i!=0 and j!=0:s[i][j]=s[i-1][j]+s[i][j-1]
        elif i!=0: s[i][j]=s[i-1][j]
        elif j!=0: s[i][j]=s[i][j-1]
a-=1
b-=1
for i in range(c):
    for j in range(c-i):
        z+=s[a-b+i][b+j]
print(z)
