a,b=map(int,input().split())
r=[]
for i in range(a):d,e,f,g=map(int,input().split());r.append([e*(10**12)+f*10**6+g,d])
r.sort(reverse=True)
for i in r:
    if i[1]==b:x=i[0]
for i in range(a):
    if r[i][0]==x:print(i+1);break
