def solution(numbers):
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])*16
    answer=''

    numbers.sort()
    for j in range(len(numbers)):
        numbers[j]=numbers[j][:(len(numbers[j])//16)]
    for j in range(len(numbers)):  
        answer+=numbers[len(numbers)-1-j]
        
    return str(int(answer))

a=int(input())
x=list(input().split())
print(solution(x))
