import sys
import time



in_put = sys.stdin.readline

        


a= int(in_put())

    
    


for i in range(a):
    c=[0, 1]
    e=[1, 0]

    b=int(in_put())
    
    if b==0:
        print(1, 0)
    else:

        for h in range(b-1):
            for zz in range(2):
                c[zz],e[zz]=e[zz],c[zz]+e[zz]
        print(e[1],e[0])



    
