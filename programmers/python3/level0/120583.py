# 중복된 숫자 개수

# 문제 설명
# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ array의 길이 ≤ 100
# 0 ≤ array의 원소 ≤ 1,000
# 0 ≤ n ≤ 1,000
# 입출력 예
# array	n	result
# [1, 1, 2, 3, 4, 5]	1	2
# [0, 2, 3, 4]	1	0
# 입출력 예 설명
# 입출력 예 #1

# [1, 1, 2, 3, 4, 5] 에는 1이 2개 있습니다.
# 입출력 예 #2

# [0, 2, 3, 4] 에는 1이 0개 있습니다.

# def solution(array, n):
#     answer = 0
#     return answer

# 순서도
# 방법 1. count로 세기

array = list(map(int, input().split()))
n = int(input())

# def solution(array, n):
#     answer = array.count(n)
#     return answer



def solution(array, n):
    answer = 0
    for k in array :
        if k == n :
            answer+=1
    return answer

print(solution(array, n))


# date 2023.03.29.