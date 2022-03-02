import sys

in_put = sys.stdin.readline



n= int(in_put())
sss= [0]*n

for i in range(n):
    sss[i]= int(in_put())


sss.sort()

for i in range(n):
    print (sss[i])
        
