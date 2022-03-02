import sys
import time



in_put = sys.stdin.readline

a=1

while (a):
    a= int(in_put())
    b= 2*a
    c= [1 for i in range(b+5)]
    p = 2
    while (p*p<=b):
        if c[p] == 1:
            for k in range(p*2, b+1, p):
                c[k]=0
        p+=1
    c[0]=c[1]=0
        
    d = b-a - c[a+1:b+1].count(0)

    




    if a:

        print(d)
        

    
