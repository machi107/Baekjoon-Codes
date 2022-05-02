input()
d=list(map(int,input().split()))
e=list(map(int,input().split()))
q=[]
for i in e:
    if i in d:d.remove(i);q.append(i)
for i in q:e.remove(i)
f=0
for i in d:
    if i-1 in e:e.remove(i-1);f+=1
    elif i+1 in e:e.remove(i+1);f+=1
print(len(d)-f)
