# 문자열 정수의 합

# 문제 설명
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ num_str ≤ 100
# 입출력 예
# num_str	result
# "123456789"	45
# "1000000"	1
# 입출력 예 설명
# 입출력 예 #1

# 문자열 안의 모든 숫자를 더하면 45가 됩니다.
# 입출력 예 #2

# 문자열 안의 모든 숫자를 더하면 1이 됩니다.

# def solution(num_str):
#     answer = 0
#     return answer

# 순서도
# 1. for문으로 num_str의 수 빼기
# 2. num_str 합하기

num_str = "123456789"

answer = 0
for i in num_str :
    answer = answer + int(i)

print(answer)




# def solution(num_str):
#     answer = 0
#     for i in num_str :
#         answer = answer + int(i)
#     return answer

# date 2023.04.23.

# 이렇게 합해도 됨!!!
# sum(map(int, list(num_str)))