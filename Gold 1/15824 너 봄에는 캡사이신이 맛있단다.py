a=int(input())
x=list(map(int,input().split()))
x.sort()
z=0
q=1
for i in range(a):
    z+=(x[i]-x[-i-1])*(q-1)
    q*=2
    q%=1000000007
print(z%1000000007)
