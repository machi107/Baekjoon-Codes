a=int(input())
x=list(map(int,input().split()))
for i in range(a):x[i]-=2
t=x[0]
for i in range(1,a):t=(t^x[i])
q=input()
if t==0:
    if q=="Whiteking":print("Blackking")
    if q=="Blackking":print("Whiteking")
else:
    print(q)
