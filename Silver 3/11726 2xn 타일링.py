a=int(input())
b=c=1
for i in range(a-1):b,c= c,b+c
print(c%10007)
