z="Case "
for i in range(int(input())):
    x=[0 for _ in range(26)]
    t=input()
    for j in range(len(t)):
        p=ord(t[j])
        if 64<p and p<91:
            x[p-65]+=1
        elif 96<p and p<123:
            x[p-97]+=1
    x=list(set(x))
    if x.count(0):print(z+str(i+1)+": Not a pangram")
    elif x.count(1):print(z+str(i+1)+": Pangram!")
    elif x.count(2):print(z+str(i+1)+": Double pangram!!")
    else:print(z+str(i+1)+": Triple pangram!!!")
