a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
month=[0,31,28,31,30,31,30,31,31,30,31,30]
t2=c+sum(month[:b])
t1=f+sum(month[:e])
if a%4==0 and b>2:t2+=1
if a%100==0 and b>2:t2-=1
if a%400==0 and b>2:t2+=1
if d%4==0 and e>2:t1+=1
if d%100==0 and e>2:t1-=1
if d%400==0 and e>2:t1+=1
if d-a>=1001:
    print('gg')
elif d-a==1000 and t1-t2>=0:
     print('gg')
else:
    ans=t1-t2+(d-a)*365
    for i in range(a,d):
        if i%4==0:ans+=1
        if i%100==0:ans-=1
        if i%400==0:ans+=1
    print("D-"+str(ans))
