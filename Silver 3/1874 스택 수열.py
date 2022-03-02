import sys
in_put=sys.stdin.readline
a=int(in_put())
num=[]
printer=[]
no=0
x=1
for _ in range(a):
    ans=int(in_put())
    while(1):
        if ans>x:
            num.append(x)
            printer.append("+")
            x+=1
        elif ans==x:
            printer.append("+")
            printer.append("-")
            x+=1
            break
        else:
            if len(num)==0 or num[-1]!=ans:
                no=1
                break
            else:
                printer.append("-")
                num.pop()
                break

if no:
    print("NO")
else:
    for i in range(len(printer)):
        print(printer[i])
    
