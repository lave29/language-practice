# 배열의 평균값

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 1,000
# 1 ≤ numbers의 길이 ≤ 100
# 정답의 소수 부분이 .0 또는 .5인 경우만 입력으로 주어집니다.
# 입출력 예
# numbers	result
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	5.5
# [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]	94.0
# 입출력 예 설명
# 입출력 예 #1

# numbers의 원소들의 평균 값은 5.5입니다.
# 입출력 예 #2

# numbers의 원소들의 평균 값은 94.0입니다.

# def solution(numbers):
#     answer = 0
#     return answer

# 순서도
# 1. 원소의 갯수 → len(numbers)
# 2. 원소의 합 → sum+=i for i in numbers


# numbers = list(map(int, input().split()))

# sum = 0

# for i in numbers :
#     sum += i

# answer=sum/len(numbers)
# print(answer)



# def solution(numbers):
#     answer = 0
    
#     sum = 0

#     for i in numbers :
#         sum += i

#     answer=sum/len(numbers)
    
#     return answer



# date 2023.04.23.


# 제출하고 알게된 사실
# 사실 예전에 활용했지만 까먹은거;;
# sum 함수가 있다는 사실;;;


numbers = list(map(int, input().split()))

answer=sum(numbers)/len(numbers)
print(answer)



# def solution(numbers):
#     answer = 0
    
#     answer=sum(numbers)/len(numbers)
    
#     return answer