a=int(input())
x=[]
for i in range(a):x.append(list(map(int,input().split())))
for i in range(1,a):
    for j in range(3):x[i][j]+=min(x[i-1][j+1:]+x[i-1][:j])
print(min(x[-1]))
