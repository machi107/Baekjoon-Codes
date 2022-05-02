a=int(input())
k=list(map(int,input().split()))
z=0
for i in range(a):
    if k[i]<4:t=0
    elif k[i]<4**2:t=1
    elif k[i]<82:t=2
    elif k[i]<82**2:t=0
    elif k[i]<50626:t=3
    elif k[i]<50626**2:t=1
    else:t=2
    z^=t
print("koosaga") if z else print("cubelover")
