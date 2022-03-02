a,b="I"+int(input())*"OI",input()
b=input().split(a)
t=x=len(b)-1
for i in range(1,x+1):
    if b[i]=="O":t+=len(a)//2
    if i:
        while(len(b[i])>1):
            if b[i][:2]=="OI":t+=1;b[i]=b[i][2:]
            else:break
print(t)
