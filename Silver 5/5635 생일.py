a,t=int(input()),[]
for i in range(a):b,c,d,e=input().split();t.append([int(e+str(int(d)+9)+str(int(c)+9)),b])
t.sort()
print(t[-1][1])
print(t[0][1])
