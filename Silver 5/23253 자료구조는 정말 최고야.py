a,b=map(int,input().split())
t="Yes"
for i in range(b):
 input()
 x=list(map(int,input().split()))
 r=x.copy()
 r.sort(reverse=1)
 if x!=r:t="No";
print(t)

# pypy3에서만 통과되는 코드
