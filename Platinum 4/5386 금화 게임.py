a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if b<c or c%2:
        if b%2:print(1)
        else:print(0)
    else:
        if (b+1)%(c+1)==0:print(c)
        elif b%(c+1)%2-1:print(0)
        else:print(1)
