a,b,c=input().split()
k=int(a[1])*10+ord(a[0])-64
s=int(b[1])*10+ord(b[0])-64
t="0"*8+"L0R"+"0"*8+"T"
for _ in range(int(c)):
 x=input();r=0;
 for i in range(len(x)):r+=t.find(x[i])-9
 q=k;k+=r
 if k==s:s+=r
 if not(10<s<90 and 0<s%10<9):s,k=k,q
 if not(10<k<90 and 0<k%10<9):k=q
print(chr(k%10+64)+str(k//10),chr(s%10+64)+str(s//10),sep="\n")
