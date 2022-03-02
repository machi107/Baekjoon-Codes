a,x=int(input()),[]
for i in range(a):x.append(int(input()))
x.sort()
for i in range(a):x[i]=x[i]*(len(x)-i)
print(max(x))
