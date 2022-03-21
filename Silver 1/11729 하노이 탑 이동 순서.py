import sys
import time

in_put = sys.stdin.readline


a= int(in_put())

def hanoi(x):

    if x != 1:
        hanoi(x-1)

        b[(2**(x-1))-1][0]=1
        b[(2**(x-1))-1][1]=3

        for i in range((2**(x-1))-1):
            for j in range(2):
                if b[i][j]==3:
                    b[i][j]=2
                elif b[i][j] == 2:
                    b[i][j]=3


        for i in range(2**(x-1),2**x-1):
            for j in range(2):
                if b[i-(2**(x-1))][j]==1:
                    b[i][j]=2
                elif b[i-(2**(x-1))][j]==2:
                    b[i][j]=3
                elif b[i-(2**(x-1))][j]==3:
                    b[i][j]=1

    else :
        b[0][0]=1
        b[0][1]=3

    





b=[[0,0] for i in range(2**a-1)]

hanoi(a)
print(len(b))

for i in range(len(b)):
    print(b[i][0], b[i][1])



