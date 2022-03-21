x,r,t,z,o=[],0,0,"",""
for i in range(10):x.append(input());r+=x[i].count("-")+x[i].count("|");z+=x[i][0];o+=x[i][9]
for i in range(0,7,3):
 for j in range(0,7,3):
  if x[i][j+1]=="-" and x[i+1][j]=="|" and x[i+3][j+1]=="-" and x[i+1][j+3]=="|":t+=1
  if i<6 and j<6 and x[i][j+1]=="-" and x[i][j+4]=="-" and x[i+1][j]=="|" and x[i+4][j]=="|" and x[i+6][j+4]=="-" and x[i+6][j+1]=="-" and x[i+1][j+6]=="|" and x[i+4][j+6]=="|":t+=1
if x[0]=="+--"*3+"+" and x[9]==x[0] and z=="+||"*3+"+" and o==z:t+=1
print((48-r)//2,t)
