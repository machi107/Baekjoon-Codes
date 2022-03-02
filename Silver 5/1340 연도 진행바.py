m=["January",'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
r=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t=525600
a=input().split()
q,w=map(int,a[3].split(':'))
e=m.index(a[0])
n=(sum(r[:e])+int((a[1][:-1]))-1)*1440+q*60+w
y=int(a[2])
if y%4:z=0
elif y%100:z=1
elif y%400:z=0
else:z=1
t+=z*1440
if e>1:n+=z*1440
print(n/t*100)
