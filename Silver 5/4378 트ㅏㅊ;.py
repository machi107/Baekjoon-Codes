while(1):
 try:
  a,x,t=" `1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./ ",input(),""
  for i in range(len(x)):t+=a[a.find(x[i])-1]
  print(t)
 except:break
