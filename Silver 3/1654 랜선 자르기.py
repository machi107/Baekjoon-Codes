import sys

in_put = sys.stdin.readline

a,b=map(int,in_put().split())
x=[]
for i in range(a):
    x.append(int(in_put()))



st=0
en= sum(x)//b


while(1):
    if en-st<=1:
        break
    count=0
    for i in range(a):
        count+=x[i]//((en+st)//2)

    
    if count>=b:
        st= (st+en)//2
    else:
        en=(en+st)//2

count=0
for i in range(a):
    count+=x[i]//en
if count>=b:
    print(en)
else:
    print(st)
