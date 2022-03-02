a=input()
t=0
while(int(a)>9):
    x=[]
    for i in range(10):
        x.append(a.count(chr(49+i))*(i+1))
    a=str(sum(x))
    t+=1
print(t)
print("NO") if int(a)%3 else print("YES")
