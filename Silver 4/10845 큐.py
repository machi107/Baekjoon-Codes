import sys
in_put = sys.stdin.readline

a=int(in_put())
x=[]
for _ in range(a):
    command =in_put().rstrip("\n")
    if command[:3] == "pus":
        x.append(int(command.split()[1]))
    elif command[:3] == "pop":
        if len(x):
            print(x[0])
            del x[0]
        else:
            print(-1)
    elif command[:3] == "siz":
        print(len(x))
    elif command[:3] == "emp":
        if len(x):
            print(0)
        else:
            print(1)
    elif command[:3] == "fro":
        if len(x):
            print(x[0])
        else:
            print(-1)
    elif command[:3] == "bac":
        if len(x):
            print(x[len(x)-1])
        else:
            print(-1)

