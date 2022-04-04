a=int(input())
while(a):
    q=[1,2,3,4,5,6,7,8,9,10]
    while(1):
        t=input()
        if t=="too high":
            for i in range(len(q)):
                if q[i]>=a:
                    q[i]=0
        elif t=="too low":
            for i in range(len(q)):
                if q[i]<=a:
                    q[i]=0
        else:
            if q.count(a):
                x="may be "
            else:
                x="is dis"
            break
        a=int(input())
    print("Stan "+x+"honest")
    a=int(input())
