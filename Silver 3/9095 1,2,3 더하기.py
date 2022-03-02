def t(n):
    if n<3:return n
    elif n==3:return 4
    elif n==4:return 7
    else:return t(n-1)*2-t(n-4)
for _ in range(int(input())):x=int(input());print(t(x))
