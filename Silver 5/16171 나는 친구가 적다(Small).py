a=input()
t=""
for i in range(len(a)):
    if a[i].isalpha():t+=a[i]
print(1if input() in t else 0)
