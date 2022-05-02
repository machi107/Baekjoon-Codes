a=int(input())
w,t,m,z,n=4*a-3,10,1,2,a-1
while(n):
    if n%2:m*=z
    z*=z
    z=z%10000
    n=n//2
while(a>=t):w+=a-t+1;w+=(a-t+1)*m;t*=10
w+=m*2*(a+1)-1
print(w%10000)
