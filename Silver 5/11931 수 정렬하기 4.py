x=[]
for i in range(int(input())):x.append(int(input()))
x.sort(reverse=True)
print(*x,sep="\n")
