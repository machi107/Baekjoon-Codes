a=int(input())
b=1
while(a>=9*b*(10**(b-1))):
    a-=9*b*(10**(b-1))
    b+=1
if b==1:a+=1
if a%b==0:print((a//b-1)%10)
else:print(str((a//b)+10**(b-1))[a%b-1])
