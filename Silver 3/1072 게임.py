x,y=map(int,input().split())
if str(y/x).count('e')==1:z=1
else:z=int((str(y/x).split('.')[1]+"00")[:2])+1
if z>=100:ans=-1
else:r=-(100*y-z*x)/(z-100)//1;ans=-r
if ans<0:ans=-1
print("%d"%ans)
