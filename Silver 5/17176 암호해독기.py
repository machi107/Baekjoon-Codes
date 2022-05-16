a=int(input())
p=list(map(int,input().split()))
for i in range(a):
    if p[i]==0:p[i]=" "
    elif p[i]<27:p[i]=chr(p[i]+64)
    else:p[i]=chr(p[i]+70)
p.sort()
x=list(input())
x.sort()
print("y" if x==p else "n")
