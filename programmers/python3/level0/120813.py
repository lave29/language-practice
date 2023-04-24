# 짝수는 싫어요

# 문제 설명
# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 100
# 입출력 예
# n	result
# 10	[1, 3, 5, 7, 9]
# 15	[1, 3, 5, 7, 9, 11, 13, 15]
# 입출력 예 설명
# 입출력 #1

# 10 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9]를 return합니다.
# 입출력 #1

# 15 이하의 홀수가 담긴 배열 [1, 3, 5, 7, 9, 11, 13, 15]를 return합니다.

# def solution(n):
#     answer = []
#     return answer

# 순서도
# 1. range를 활용해서 n 이하의 모든 수를 나오게 함
# 2. %2 !=0 일 경우는 홀수 이므로 이때의 모든 수를 answer의 배열에 담으면 끝

n = int(input('정수 n:'))

def solution(n):
    answer = []
    for i in range(n+1) :
        if i % 2 != 0 :
            answer.append(i)
    return answer

print(solution(n))



# date 2023.04.24.