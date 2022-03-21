a,b=map(int,input().split())
while(a+b):
    t=[0 for i in range(a)]
    q=0
    while(t.count(0)!=a-1 or b!=0):
        if b==0:
            b+=t[q]
            t[q]=0
        else:
            b-=1
            t[q]+=1
        q+=1
        q=q%a
    print(t.index(max(t)))
    a,b=map(int,input().split())
