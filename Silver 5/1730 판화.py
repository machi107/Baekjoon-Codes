a=int(input())
x=[['.' for _ in range(a)] for _ in range(a)]
t=[0,0]
m=input()
for i in range(len(m)):
    if m[i]=="U" and t[0]:
        if x[t[0]][t[1]]=="-":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="|"
        t[0]-=1
        if x[t[0]][t[1]]=="-":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="|"
        
    elif m[i]=="D" and t[0]!=a-1:
        if x[t[0]][t[1]]=="-":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="|"
        t[0]+=1
        if x[t[0]][t[1]]=="-":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="|"
    elif m[i]=="L" and t[1]:
        if x[t[0]][t[1]]=="|":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="-"
        t[1]-=1
        if x[t[0]][t[1]]=="|":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="-"
    elif m[i]=="R" and t[1]!=a-1:
        if x[t[0]][t[1]]=="|":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="-"
        t[1]+=1
        if x[t[0]][t[1]]=="|":
            x[t[0]][t[1]]="+"
        elif x[t[0]][t[1]]==".":
            x[t[0]][t[1]]="-"
for i in range(a):
    for j in range(a):print(x[i][j],end="")
    print("")
