a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
g,h=map(int,input().split())
ce=((c-e)**2+(d-f)**2)**0.5
cg=((c-g)**2+(d-h)**2)**0.5
eg=((g-e)**2+(h-f)**2)**0.5
ae=((a-e)**2+(b-f)**2)**0.5
ag=((g-a)**2+(h-b)**2)**0.5
ac=((a-c)**2+(b-d)**2)**0.5
x=(min(ae+eg+cg,ae+ce+cg))
y=(min(ag+ce+cg,ag+ce+eg))
z=(min(ac+eg+ce,ac+eg+cg))
print(int(min(x,y,z)//1))
