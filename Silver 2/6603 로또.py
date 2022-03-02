import itertools
a=list(map(int,input().split()))[1:]
while(a):
    
    x=list(itertools.combinations(a,6))
    for i in range(len(x)):
        for j in range(len(x[i])):
           print(x[i][j],end=" ")
        print()
    a=list(map(int,input().split()))[1:]
    if a:
        print()
        
