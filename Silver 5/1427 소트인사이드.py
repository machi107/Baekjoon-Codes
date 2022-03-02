import sys

in_put = sys.stdin.readline


a=in_put().rstrip("\n")

b=list(a)
b.sort(reverse=True)

for i in range(len(b)):
    print(b[i],end="")
