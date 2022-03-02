import sys

in_put = sys.stdin.readline



n= int(in_put())
b=[0]*10001


for i in range(n):
    b[int(in_put())] +=1

for i in range(10001):
    if b[i] !=0:
        for h in range(b[i]):
            print(i)
        
