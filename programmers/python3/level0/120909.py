# 제곱수 판별하기

# 문제 설명
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 1,000,000
# 입출력 예
# n	result
# 144	1
# 976	2
# 입출력 예 설명
# 입출력 예 #1

# 144는 12의 제곱이므로 제곱수입니다. 따라서 1을 return합니다.
# 입출력 예 #2

# 976은 제곱수가 아닙니다. 따라서 2를 return합니다.

# def solution(n):
#     answer = 0
#     return answer

# 순서도

n = int(input('정수 n:'))

def solution(n):
    answer = 2
    for i in range(1, n+1) :
        if n / i == i :
            answer = 1
    
    return answer

print(solution(n))


# 0.5승이라니...;; 생각도 못했다
# 게다가 is_integer()라는 정수 여부 판단하는 함수도 있다니;;;
# 정수면 True, 정수가 아니면 False가 나오는듯
# return 1 if (n ** 0.5).is_integer() else 2

# 아니면 math를 import해서 제곱근 sqrt() 함수도 있음;;
# 왜 제곱근을 생각 안했냐;;;


# date 2023.04.24.