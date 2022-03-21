def p(c,q):
 t=0
 while(c):t+=c//q;c=c//q
 return t
a,b=map(int,input().split())
b=min(a-b,b)
r=a-b
print(min(p(a,5)-p(b,5)-p(r,5),p(a,2)-p(b,2)-p(r,2)))
