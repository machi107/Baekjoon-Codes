a=int(input())
z=0
for i in range(a):
    b,c=map(int,input().split())
    q=0
    if b%2:q=b
    for j in range((c+b%2*3)%4):q^=c+b-j-1
    z^=q
print("koosaga") if z else print("cubelover")
