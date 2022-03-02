import sys

def solution(s):
    a=0
    for i in range (len(s)):
        if s[i]=="(":
            a+=1
        else:
            a-=1
        if a<0:
            return False
    
    return not (a!=0)

in_put = sys.stdin.readline

for _ in range(int(in_put())):
    if solution(in_put().rstrip("\n"))==False:
        print("NO")
    else:
        print("YES")
