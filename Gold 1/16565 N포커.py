a=int(input())
ans=0
for i in range(a//4):
    r=1
    for k in range(i+1):r*=13-k;r/=k+1
    for k in range(a-4*(i+1)):r*=52-4*(i+1)-k;r/=k+1
    if i%2:r=-r
    ans+=r
print(int(ans%10007))
