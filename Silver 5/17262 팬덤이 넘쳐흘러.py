a=0
b=9**9
for i in range(int(input())):
    c,d=map(int,input().split())
    if c>=a:a=c
    if d<=b:b=d
print(max(a-b,0))
