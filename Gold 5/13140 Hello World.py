import itertools
a,b,z=input(),list(range(10)),0
x=list(itertools.permutations(b,7))
for i in range(604800):
    h,w,e,o,l,r,d=x[i][0],x[i][1],x[i][2],x[i][3],x[i][4],x[i][5],x[i][6]
    if int(a)==(h+w)*10000+(e+o)*1000+o+l*120+r*100+d and h*w:z=1;break
l=str(l)
o=str(o)
if z:print("  "+str(h)+str(e)+l+l+o);print("+ "+str(w)+o+str(r)+l+str(d));print("-"*7);print(" "*(7-len(a))+a)
else:print("No Answer")
