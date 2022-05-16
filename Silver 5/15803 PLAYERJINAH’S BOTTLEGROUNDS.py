a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
x,y,o,u,p,q=c-a,c-e,d-b,f-b,e-a,d-f
z=1
if (x+y)*(o+u)==0 or o and u and x/o==p/u:z=0
print("WINNER "*2+"CHICKEN DINNER!" if z else "WHERE IS MY CHICKEN?")
