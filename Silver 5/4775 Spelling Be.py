import sys
q=sys.stdin.readline

a=int(input())
x=['-1']
for i in range(a):x.append(q().rstrip("\n"))
t=0
r=int(input())
for i in range(r):
    z=[]
    t=q().rstrip("\n")
    while(t!='-1'):
        if not t in x:z.append(t)
        t=q().rstrip("\n")
    if len(z):
        print("Email {0} is not spelled correctly.".format(i+1))
        for h in range(len(z)):print(z[h])
    else:print("Email {0} is spelled correctly.".format(i+1))
print("End of Output")
