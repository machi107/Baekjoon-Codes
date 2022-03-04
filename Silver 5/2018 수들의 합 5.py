n=int(input())
r=0
for i in range(1,n,2):
    if n/i==n//i and n/i-i/2>0:r+=1
for j in range(2,n,2):
    if n/j%1==0.5 and n/j-j/2> 0:r+=1
if n==1:r+=1
print(r)
