a,b=map(int,input().split())
t=b/2*(b+1)
if(a-t)%b:b+=1
print(-1if t>a else b-1)
