import sys

in_put = sys.stdin.readline


z = int(in_put())


for i in range(z):
    a,b = map(int, in_put().split())

    if (b-a <3):
        print(b-a)
    else:
        
        n=b-a
        coun= 1
        while(n>=1):
            n= n-coun
            if (n<1):
                coun +=0.5
                break
            
            n= n-coun
            coun +=1
            
        print(int((coun-1)*2))
            
