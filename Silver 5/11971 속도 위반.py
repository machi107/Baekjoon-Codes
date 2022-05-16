a=[0 for i in range(100)]
b,c=map(int,input().split())
q=0
for i in range(b):
    d,e=map(int,input().split())
    for j in range(q,d+q):
        a[j]=e
    q=j+1
q=0
for i in range(c):
    d,e=map(int,input().split())
    for j in range(q,d+q):
        a[j]=max(e-a[j],0)
    q=j+1
print(max(a))
