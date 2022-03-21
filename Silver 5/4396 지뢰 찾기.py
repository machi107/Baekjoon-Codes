a=int(input())
x=[]
c=0
for i in range(a):
    x.append(list(input()))

for i in range(a):
    for j in range(a):
        if x[i][j]=='.':
            t=0
            if i>0:
                if x[i-1][j]=="*":t+=1
                if j>0 and x[i-1][j-1]=="*":t+=1
                if j<a-1 and x[i-1][j+1]=="*":t+=1
            if j>0 and x[i][j-1]=="*":t+=1
            if j<a-1 and x[i][j+1]=="*":t+=1
            if i<a-1:
                if x[i+1][j]=="*":t+=1
                if j>0 and x[i+1][j-1]=="*":t+=1
                if j<a-1 and x[i+1][j+1]=="*":t+=1
            x[i][j]=t


y=[]
for i in range(a):
    ttt=input()
    qqq=""
    for j in range(a):
        if ttt[j]=="x":
            if x[i][j]=="*":c=1;qqq+="*"
            else:qqq+=str(x[i][j])
        else:qqq+="."
    y.append(qqq)
if c:
    for i in range(a):
        for j in range(a):
            if x[i][j]=="*":
                y[i]=y[i][:j]+"*"+y[i][j+1:]

for i in range(a):
    print(y[i])
