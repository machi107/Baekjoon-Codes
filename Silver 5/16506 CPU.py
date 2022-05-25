for i in range(int(input())):
    k,a,b,c=input().split()
    k=k.replace("ADD","0000")
    k=k.replace("SUB","0001")
    k=k.replace("MOV","0010")
    k=k.replace("AND","0011")
    k=k.replace("OR","0100")
    k=k.replace("NOT","0101")
    k=k.replace("MULT","0110")
    k=k.replace("LSFTL","0111")
    k=k.replace("LSFTR","1000")
    k=k.replace("ASFTR","1001")
    k=k.replace("RL","1010")
    k=k.replace("RR","1011")
    k=k.replace("C","1")
    if len(k)==4:k+="0"
    a=int(a)
    b=int(b)
    c=int(c)
    a=bin(a)
    b=bin(b)
    c=bin(c)
    a=a[2:]
    b=b[2:]
    c=c[2:]
    if len(a)<4:a="0"*(4-len(a))+a
    if len(b)<3:b="0"*(3-len(b))+b
    if len(c)<4:c="0"*(4-len(c))+c
    if k[4]=="0":c=c[1:]+"0"
    print(k+a+b+c)

