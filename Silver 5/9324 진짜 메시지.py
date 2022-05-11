for i in range(int(input())):
    t=[1 for i in range(26)]
    z=input()
    q="OK"
    for i in range(len(z)):
        n=ord(z[i])-65
        t[n]+=1
        if t[n]%4==0:
            if i+1==len(z) or z[i+1]!=z[i]:q="FAKE"
    print(q)
