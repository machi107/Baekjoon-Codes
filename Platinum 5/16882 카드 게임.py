a=int(input())
t=list(map(int,input().split()))
x=[0 for i in range(10**5)]
for i in range(a):x[t[i]-1]+=1
x=list(set(x))
r=0
for u in range(len(x)):
    if x[u]%2:
        r+=1
        break
print("koosaga") if r else print("cubelover")   
