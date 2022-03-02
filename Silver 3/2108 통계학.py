import sys
import time

in_put = sys.stdin.readline



n= int(in_put())
c=[0]*8001

for i in range(n):
    c[int(in_put())+4000]+=1


aa=0
bb=n/2
cc=0
dd=0
ee=0
count = 0
max = 4001
min = -4001

for j in range(8001):
    if c[j]!=0:
        if min == -4001:
            min = j-4000
        max = j-4000
        


        
        
        if bb >0:
            bb-=c[j]
            cc=(j-4000)
            
        for q in range(c[j]):
            aa+=j-4000

        if ee < c[j] :
            dd = j-4000
            ee = c[j]
            count = 1
            
        elif ee== c[j] and count:
            count=0
            ee=c[j]
            dd =j-4000

            
            

aa=round(aa/n)



print(aa)
print(cc)
print(dd)
print(max-min)
