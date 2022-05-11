a=input()
z="hate"
x="UCPC"
r=0
for i in range(len(a)):
    if a[i]==x[r]:r+=1
    if r==4:z="love";break
print("I "+z+" "+x)
