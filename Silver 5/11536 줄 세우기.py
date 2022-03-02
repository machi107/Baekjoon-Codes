a=int(input())
x=[]
for i in range(a):x.append(input())
t=x.copy()
w=x.copy()
r="CREASING"
t.sort()
w.sort(reverse=True)
if t==x:r="IN"+r
elif w==x:r="DE"+r
else:r="NEITHER"
print(r)
