t=[1,2]
while(t[-1]<10**15):t.append(t[-1]+t[-2])
x=int(input())
for i in range(1,len(t)+1):
    if x in t:break
    if x>t[-i]:x-=t[-i]
print(x)
