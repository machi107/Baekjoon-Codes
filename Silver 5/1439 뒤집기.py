a=input()
d=[2]
for i in range(len(a)):
    if d[-1]!=a[i]:
        d.append(a[i])
t=d.count('1')
print(min(len(d)-t-1,t))
