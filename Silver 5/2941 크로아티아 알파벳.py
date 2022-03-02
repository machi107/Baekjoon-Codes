import sys

in_put = sys.stdin.readline

a=['c=','c-','d-','lj','nj','s=','z=']
b='dz='


word = in_put().rstrip('\n')

count=(len(word))

for i in range(len(a)):
    count-=word.count(a[i])
count -= word.count(b)

print(count)
