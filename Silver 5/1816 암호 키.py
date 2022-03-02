a=int(input())
for i in range(a):
    x,t=int(input()),"YES"
    for h in range(2,10**6):
        if x%h==0:t="NO";break
    print(t)
