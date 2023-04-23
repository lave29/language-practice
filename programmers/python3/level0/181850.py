# 정수 부분

# 문제 설명
# 실수 flo가 매개 변수로 주어질 때, flo의 정수 부분을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ flo ≤ 100
# 입출력 예
# flo	result
# 1.42	1
# 69.32	69
# 입출력 예 설명
# 입출력 예 #1

# 1.42의 정수 부분은 1입니다.
# 입출력 예 #2

# 69.32의 정수 부분은 69입니다.

# def solution(flo):
#     answer = 0
#     return answer

# 순서도
# 방법 1. math.floor을 활용하여 소수점 아래를 버린다.

# import math

# flo = float(input('실수를 입력하세요:'))

# flo=math.floor(flo)

# print(flo)


# 방법 2. str()해서 split('.')

# flo = float(input('실수를 입력하세요:'))

# flo = str(flo).split('.')
# print(flo[0])



# import math

# def solution(flo):
#     answer = 0

#     answer=math.floor(flo)
    
#     return answer


# date 2023.04.23.

# 멍청이....이거 int만 해도 돼;;; 아니면 //

flo = float(input('실수를 입력하세요:'))

flo=int(flo)
# flo=flo//1

print(flo)