import sys

in_put = sys.stdin.readline

c=[]
n,m= map(int,in_put().split())
for i in range(n):
    line=[]
    color = in_put().rstrip("\n")
    for j in range(m):
        line.append(color[j])
    c.append(line)
aa=0
for a in range(n-7):
    for b in range(m-7):
        ee=0
        ff=0
        for i in range(8):
            for j in range(8):
                if (a+i+b+j)%2:
                    ee+=c[a+i][b+j].count("W")
                    ff+=c[a+i][b+j].count("B")
                else:
                    ee+=c[a+i][b+j].count("B")
                    ff+=c[a+i][b+j].count("W")
        
        if aa<max(ee,ff):
            aa=max(ee,ff)
print(64-aa)

## 막 시작할때 써냈던 코드라서 굉장히 더럽다.
