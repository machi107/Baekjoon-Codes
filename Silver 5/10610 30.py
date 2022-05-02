a=list(input())
a.sort(reverse=True)
t=list(map(int,a))
print(''.join(a))if sum(t)%3==0 and a.count('0') else print(-1)
