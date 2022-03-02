import sys
in_put = sys.stdin.readline


a,b=map(int,in_put().split(" "))
x=-1
while(a+1>=b):
    if b%2 and a%b==0:
        if a/b-b//2>=0:
            x=b
            break

    if b%2==0 and a/b%1==0.5:
        if a/b-b/2>=-1:
            x=b
            break
    if b==100:
        break
    b+=1

if x%2:
    for i in range(a//x-x//2,a//x+x//2+1):
        print(i,end=" ")

else:
    for i in range(a//x-x//2+1,a//x+x//2+1):
        print(i,end=" ")

if x==-1:
    print(x)
