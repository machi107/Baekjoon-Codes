import sys
in_put=sys.stdin.readline
while(1):
    a=input()
    if a==".":
        break
    t=0
    b=c=0
    k=[]
    for i in range(len(a)):
        if a[i]=="[":
            b+=1
            k.append(1)
        elif a[i]=="]":
            b-=1
            if len(k) and k.pop()==2:
                t=1
                break
            
        elif a[i]=="(":
            c+=1
            k.append(2)
        elif a[i]==")":
            c-=1
            if len(k) and k.pop()==1:
                t=1
                
                break

        if c<0 or b<0:
            t=1
            break
    if t or c+b:
        print("no")
    else:
        print("yes")


        
