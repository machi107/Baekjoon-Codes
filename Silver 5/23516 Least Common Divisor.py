a,b,t=input(),input(),0
for i in range(1,len(a)+1):
    if a[:i]*(len(a)//i)==a and a[:i]*(len(b)//i)==b:t=1;break
if t:print(a[:i])
else:print("No solution")
