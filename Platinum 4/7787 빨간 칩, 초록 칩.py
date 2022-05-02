a,b=map(int,input().split())
a=bin(a)
b=bin(b)
a=len(a)-len(a.rstrip("0"))
b=len(b)-len(b.rstrip("0"))
t="B"
if a^b:t="A"
print(t,"player wins")
