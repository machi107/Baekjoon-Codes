input()
x=list(map(int,input().split()))
z=sum(x)
q=0
for i in x:q+=(z-i)*i
print(q//2)
