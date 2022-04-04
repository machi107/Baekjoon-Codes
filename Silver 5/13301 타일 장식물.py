x=[1,1]
t=int(input())
for i in range(t-2):x.append(x[-1]+x[-2]);
if t>3:print(x[-1]*3+(x[-2]+x[-3])*2+x[-4]*1)
elif t==3:print(10)
else:print(t*2+2)
