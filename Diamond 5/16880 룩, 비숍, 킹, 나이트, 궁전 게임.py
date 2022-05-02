def g(x,y):return (x+y)%3+((x//3)^(y//3))*3
def r(x,y):return x^y
def b(x,y):return min(x,y)
def k(x,y):return min(x,y)%2*2+(x+y)%2
def n(x,y):
    r=min(x,y)%3
    t=max(x,y)-min(x,y)//3
    if t<r*2:r-=1
    return(r%3)
z=int(input())
l=0
for i in range(z):
    x,y,t=input().split()
    x=int(x)
    y=int(y)
    if t=="B":l^=b(x,y)
    elif t=="R":l^=r(x,y)
    elif t=="K":l^=k(x,y)
    elif t=="N":l^=n(x,y)
    elif t=="P":l^=g(x,y)
print("koosaga") if l else print("cubelover")
