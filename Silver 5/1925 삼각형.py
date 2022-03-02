a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
x,y,o,u,p,q=c-a,c-e,d-b,f-b,e-a,d-f
l1=x*x+o*o
l2=p*p+u*u
l3=y*y+q*q
t1=max(l1,l2,l3)
t3=min(l1,l2,l3)
t2=l1+l2+l3-t1-t3
z="Triangle"
if l1==l2 or l2==l3 or l1==l3:z="2"+z
if t1 > t3+t2:z="Dunkak"+z
elif t1==t3+t2:z="Jikkak"+z
else:z="Yeahkak"+z
if (x+y)*(o+u)==0 or o and u and x/o==p/u:z="X"
print(z)
