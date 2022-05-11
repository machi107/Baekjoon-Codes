a=[0,1]
for i in range(50):a.append(a[-1]+a[-2])
t=int(input())
print(*a[t-1:t+1])
