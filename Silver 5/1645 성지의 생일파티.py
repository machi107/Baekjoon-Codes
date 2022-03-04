a,x=int(input()),[]
for i in range(a):x.append(int(input()))
x.sort()
for i in range(a):
    if x[i]<i+1:break
print(i+1)
