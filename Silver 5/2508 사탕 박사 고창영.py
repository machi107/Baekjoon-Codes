for i in range(int(input())):
    input()
    b,c=map(int,input().split())
    box=[]
    for i in range(b):box.append(input());ans=0
    for i in range(b):
        for j in range(c):
            if box[i][j]=='o':
                if  j>0 and box[i][j-1]=='>' and j<c-1 and box[i][j+1]=="<"or i>0 and box[i-1][j]=='v' and i<b-1 and box[i+1][j]=="^":ans+=1
    print(ans)
