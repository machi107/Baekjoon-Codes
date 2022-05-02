a=int(input())
for i in range(a):
    b,c,d=input().split()
    b=int(b)
    c=int(c)
    e=[['3' for _ in range(c+2)]]
    for j in range(b):
        f=['3']
        for q in range(c):
            f.append(d[c*j+q])
        f.append('3')
        e.append(f)
    e.append(['3' for _ in range(c+2)])

    t=""
    x,y=1,1
    pe=[[0,1],[1,0],[0,-1],[-1,0]]
    q=0
    zz=4
    while(zz):
        if e[x][y]!='3':t+=e[x][y];e[x][y]='3'
        if e[x+pe[q][0]][y+pe[q][1]]!='3':zz=4;x+=pe[q][0];y+=pe[q][1]
        else:
            q+=1
            zz-=1
            if q==4:q-=4
    while(len(t)%5!=0):t+="0"
    k=""
    for i in range(len(t)//5):
        k+=chr(int(t[i*5:(i+1)*5],2)+64)
    k=k.replace("@"," ")
    k=k.rstrip(" ")
    print(k)
        
