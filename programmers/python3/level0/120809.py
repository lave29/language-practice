# 배열 두배 만들기

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# -10,000 ≤ numbers의 원소 ≤ 10,000
# 1 ≤ numbers의 길이 ≤ 1,000
# 입출력 예
# numbers	result
# [1, 2, 3, 4, 5]	[2, 4, 6, 8, 10]
# [1, 2, 100, -99, 1, 2, 3]	[2, 4, 200, -198, 2, 4, 6]
# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 4, 5]의 각 원소에 두배를 한 배열 [2, 4, 6, 8, 10]을 return합니다.
# 입출력 예 #2

# [1, 2, 100, -99, 1, 2, 3]의 각 원소에 두배를 한 배열 [2, 4, 200, -198, 2, 4, 6]을 return합니다.

# def solution(numbers):
#     answer = []
#     return answer

# 순서도
# 1. for문으로 numbers의 원소를 하나씩 가져오기
# 2. 가져온 원소를 2배해서 다시 배열에 넣기 → append()



numbers = list(map(int, input('numbers의 원소를 입력하세요: ').split()))

answer=[]

for i in numbers :
    answer.append(i*2)

print(answer)



# def solution(numbers):
#     answer = []
    
#     for i in numbers :
#         answer.append(i*2)
    
#     return answer



# date 2023.04.23.


# numpy와 lamda, 리스트 컴프리헨션 방법을 쓰는 분들도 있음..!!
# 공부하자!!