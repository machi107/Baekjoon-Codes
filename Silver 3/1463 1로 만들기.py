import sys


in_put = sys.stdin.readline
a= int(in_put())
count=[0 for _ in range(a+1)]
count[1]=0

for i in range(2,a+1):
    b=c=d=50000000
    if i%3==0:
        b=count[i//3]
    if i%2==0:
        c=count[i//2]

    d= count[i-1]

    count[i]=min(b,c,d)+1


    

print(count[a])

    
