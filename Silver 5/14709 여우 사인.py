x=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    x.append(a)
    x.append(b)
x.sort()
print("Woof-meow-tweet-squeek" if x!=[1,1,3,3,4,4] else "Wa-"+"pa-"*5+"pow!")
