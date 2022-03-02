a=int(input())
c=[1,1,1,2,2]
for i in range(99):c.append(c[i]+c[i+4])
for i in range(a):print(c[int(input())-1])
