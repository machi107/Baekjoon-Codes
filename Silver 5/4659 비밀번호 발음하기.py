t=input()
while(t!="end"):
 s,x,r=1,"","aeiou"
 for i in range(len(t)):
  if r.count(t[i]):x+="0"
  else:x+="1"
  if i and t[i]==t[i-1] and t[i]!='e' and t[i]!='o':s=0
 if t.count('a')+t.count('e')+t.count('o')+t.count('i')+t.count('u')==0:s=0
 if x.count("000") or x.count("111"):s=0
 z="not "
 if s:z=""
 print("<{0}> is {1}acceptable.".format(t,z))
 t=input()
