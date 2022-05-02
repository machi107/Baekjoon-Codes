a=[0,1,1,1,2,2,0]
p=int(input())
for i in range(7,p+1):
    t=[]
    t.append(a[-3])
    t.append(a[-4])
    t.append(a[-5])
    for j in range(i-6):t.append(a[j+1]^a[-6-j])
    for k in range(len(t)+1):
        if not k in t:a.append(k);break
print(1)if a[p] else print(2)
