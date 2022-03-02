import sys
import math

in_put = sys.stdin.readline


b= int(in_put())

a= list(map(int,in_put().split()))
count =b


for i in range(b):
    if a[i] > 1:
        for j in range(2,a[i]):
            if (a[i]/j==a[i]//j):
                count-=1
                break;
    else:
        count-=1
            
print(count)
