a,b,c=map(int,input().split())
x=[a+i*15 for i in range(28*19)]
y=[b+i*28 for i in range(15*19)]
z=[c+i*19 for i in range(15*28)]
print(list(set(x)&set(y)&set(z))[0])
