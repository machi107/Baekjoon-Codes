a,b,c,d,e,f=map(int,input().split())
x,y,o,u,p,j,s=c-a,c-e,d-b,f-b,e-a,f-d,0.5
r=x*x+o*o
t=p*p+u*u
q=y*y+j*j
z=max(r,t,q)**s-min(r,t,q)**s
if(x+y)*(o+u)==0 or o and u and x/o==p/u:z=-s
print(z+z)
