c=0
q=[]
for i in range(11):a,b=map(int,input().split());q.append([a,b])
q.sort()
r=0
for i in range(11):c+=q[i][1]*20+r+q[i][0];r+=q[i][0]
print(c)
