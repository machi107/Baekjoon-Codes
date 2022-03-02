import sys
import itertools
in_put = sys.stdin.readline

a=int(in_put())
x=[]
t=1
while(1):
    if t*t>a:
        break
    x.append(t*t)
    t+=1
ans=4
if x.count(a):
    ans=1
else:
    py=[]
    num=0
    while(1):
        if x[num]>=a//3:
            py.append(x[num])
        num+=1
        if num>=len(x):
            break
    z=[]
    zz=[]
    if ans==4:
        for i in range(1):
            for aa in range(len(py)):
                for bb in range(len(x)):
                    z.append(py[aa]+x[bb])
            if z.count(a):
                ans=2
                break
    if ans==4:
        for aa in range(len(z)):
            for bb in range(len(x)):
                if a==(z[aa]+x[bb]):
                    ans=3
                    break
            if ans==3:
                break
print(ans)


## pypy3 에서만 통과한 코드

