a,b=map(int,input().split())


s=[[0 for _ in range(32)] for _ in range(32)]
s[0][0]=1
for i in range(32):
    for j in range(32-i):
        if i!=0 and j!=0:s[i][j]=s[i-1][j]+s[i][j-1]
        elif i!=0: s[i][j]=s[i-1][j]
        elif j!=0: s[i][j]=s[i][j-1]
print(s[b-1][a-b])
