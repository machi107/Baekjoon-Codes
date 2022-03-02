import sys
import math

in_put = sys.stdin.readline


a= int(in_put())
b= int(in_put())
sum =0
ans = 0
if b<=1:
    a=3
if (a<=2):
    sum+=2
    ans+=2
    a=3


for i in range(a,b+1):
    count = 1

    for j in range (2,i):
        if (i//j == i/j):
            count = 0
            break

    if (count == 1):
        sum += i
        
    if (ans ==0  and count == 1):
        ans +=i

if (sum != 0):
    print(sum)
    print(ans)
else:
    print(-1)

    
