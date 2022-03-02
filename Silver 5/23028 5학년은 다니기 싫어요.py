a,b,c=map(int,input().split())
z,x,t=8-a,[],"Nae ga wae"
for i in range(10):x.append(list(map(int,input().split())))
for i in range(z):b+=x[i][0]*3;c+=(x[i][0]+min(6-x[i][0],x[i][1]))*3
if b>65 and c>129:t="Nice"
print(t)
