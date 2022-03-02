a,b,c=map(int,input().split())
for i in range(c-1):a=a*10%b
print(a*10//b%10)
