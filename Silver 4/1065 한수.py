import sys

in_put = sys.stdin.readline

def hansu(a):
    if a<100:
        print(a)
    else:
        b=99
        for i in range(100,a+1):
            if i//100- (i//10)%10 == (i//10)%10-i%10:
                b+=1
        print(b)

hansu(int(in_put()))
