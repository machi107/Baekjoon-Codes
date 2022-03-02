import sys

in_put = sys.stdin.readline

a=[]
for _ in range(int(in_put())):
    s=in_put().rstrip("\n")
    x = s[:3]
    if x=="pus":
        a.append(s[s.index(" ")+1:])

    elif x=="top":
        if len(a):
            print(a[-1])
        else:
            print(-1)

    elif x=="siz":
        print(len(a))

    elif x=="pop":
        if len(a):
            print(a[-1])
            a=a[:-1]
        else:
            print(-1)

    else:
        if len(a):
            print(0)
        else:
            print(1)

    
