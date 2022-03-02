a=input()
a=a.replace("6","9")
t=0
for i in range(9):
    t=max(t,a.count(str(i)))
t=max(t,(a.count("9")-1)//2+1)
print(t)
