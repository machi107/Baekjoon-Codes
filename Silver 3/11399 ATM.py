import sys

in_put = sys.stdin.readline

a= int(in_put())

b=list(map(int,in_put().split(" ")))

b.sort()

sum=0
for i in range(a):
    sum+=b[i]*(a-i)
print(sum)


