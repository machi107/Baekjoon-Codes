a=input()
b=int(input())
r=0
for i in range(b):
    t=input();
    l=len(t)
    t+=t
    if len(a)<=l and t.count(a):r+=1
print(r)
