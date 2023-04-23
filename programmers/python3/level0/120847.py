# 최댓값 만들기 (1)

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers의 길이 ≤ 100
# 입출력 예
# numbers	result
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744
# 입출력 예 설명
# 입출력 예 #1

# 두 수의 곱중 최댓값은 4 * 5 = 20 입니다.
# 입출력 예 #1

# 두 수의 곱중 최댓값은 31 * 24 = 744 입니다.

# def solution(numbers):
#     answer = 0
#     return answer

# 순서도
# 1. sort()로 오름차순으로 나열
# 2. reverse()로 내림차순으로 나열
# 3. numbers[0]는 최댓값, numbers[1]은 그다음 최댓값이므로 이를 곱하면 됨

numbers = list(map(int, input().split()))

def solution(numbers):
    answer = 0
    numbers.sort()
    numbers.reverse()
    answer = numbers[0]*numbers[1]
    return answer

print(solution(numbers))

#sort하고 -2, -1이 곧 맨 뒤에서다;;; 쳇 ㅡ3ㅡ;;;
#공부가 필요해

#date 2023.04.23.