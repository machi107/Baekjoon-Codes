a,b=map(int,input().split())
while(a+b):
    c=0
    x=[]
    for i in range(a):
        x.append(list(input()))

    for i in range(a):
        r=""
        for j in range(b):
            if x[i][j]=='.':
                t=0
                if i>0:
                    if x[i-1][j]=="*":t+=1
                    if j>0 and x[i-1][j-1]=="*":t+=1
                    if j<b-1 and x[i-1][j+1]=="*":t+=1
                if j>0 and x[i][j-1]=="*":t+=1
                if j<b-1 and x[i][j+1]=="*":t+=1
                if i<a-1:
                    if x[i+1][j]=="*":t+=1
                    if j>0 and x[i+1][j-1]=="*":t+=1
                    if j<b-1 and x[i+1][j+1]=="*":t+=1
                x[i][j]=t
            r+=str(x[i][j])
        print(r)
    a,b=map(int,input().split())
