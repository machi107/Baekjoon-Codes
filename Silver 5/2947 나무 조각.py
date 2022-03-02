x=input().split()
while(x!=["1","2","3","4","5"]):
    for i in range(4):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]
            print(x[0],x[1],x[2],x[3],x[4])
