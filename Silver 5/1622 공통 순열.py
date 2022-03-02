while True:
 try:
  x=[0 for i in range(26)]
  y=[0 for i in range(26)]
  r,u,o=input(),input(),""
  for i in range(len(r)):x[ord(r[i])-97]+=1
  for i in range(len(u)):y[ord(u[i])-97]+=1
  for i in range(26):
   if x[i] and y[i]:o+=chr(i+97)*min(x[i],y[i])
  print(o)
 except:break
