s=0
z=input()
for i in range(26):
    x=[0 for _ in range(26)]
    q=z.index(chr(i+65))
    while(z[q+1]!=chr(i+65)):
        x[ord(z[q+1])-65]+=1
        q+=1
    s+=x.count(1)
print(s//2)
