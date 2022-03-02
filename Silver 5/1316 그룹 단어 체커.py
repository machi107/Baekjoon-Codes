import sys

in_put = sys.stdin.readline


num = int(in_put())
j=0

for i in range(num):
    word = in_put().rstrip('\n')
    while (len(word)>1):
        counter=1
        for j in range(word.count(word[0])):
            if word[j] != word[0]:
                counter =0

        if counter ==0:
            num-=1
            break


        else :
            word=word.lstrip(word[0])
        


print (num)
