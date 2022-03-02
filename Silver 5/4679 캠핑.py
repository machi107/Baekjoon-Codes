x=1
while(1):
    a,b,c=map(int,input().split())
    if a+b+c==0:
        break
    print("Case {0}: {1}".format(x,a*(c//b)+min(c%b,a)))
    x+=1
