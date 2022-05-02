a,t=int(input()),0
for i in range(a):x,y=map(int,input().split());t^=(x+y)%3+((x//3)^(y//3))*3
print("koosaga") if t else print("cubelover")
