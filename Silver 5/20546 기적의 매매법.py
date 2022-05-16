a=b=int(input())
x=list(map(int,input().split()))
z=0
q=0
for i in x:
    if i<=a:z+=a//i;a=a%i
a+=z*x[13]
for i in range(3,14):
    if x[i-3]>x[i-2] and x[i-2]>x[i-1] and x[i-1]>x[i]:q+=b//x[i];b=b%x[i]
    elif x[i-3]<x[i-2] and x[i-2]<x[i-1] and x[i-1]<x[i]:b+=q*x[i];q=0
b+=q*x[13]
if a>b:print("BNP")
elif a<b:print("TIMING")
else:print("SAME"*2)
