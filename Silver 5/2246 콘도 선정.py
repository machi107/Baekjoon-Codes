a=int(input())
t=[]
for i in range(a):t.append(list(map(int,input().split())))
t.sort()
c=1
q=t[0][1]
for i in range(a):
    if t[i][1]<q:c+=1;q=t[i][1]
print(c)
