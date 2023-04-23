# 분수의 덧셈

# 문제 설명
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 <numer1, denom1, numer2, denom2 < 1,000
# 입출력 예
# numer1	denom1	numer2	denom2	result
# 1	2	3	4	[5, 4]
# 9	2	1	3	[29, 6]
# 입출력 예 설명
# 입출력 예 #1

# 1 / 2 + 3 / 4 = 5 / 4입니다. 따라서 [5, 4]를 return 합니다.
# 입출력 예 #2

# 9 / 2 + 1 / 3 = 29 / 6입니다. 따라서 [29, 6]을 return 합니다.

# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     return answer

# 순서도
# 1. 분수 덧셈을 할 때는 통분 함
# 2. 기약 분수로 나타내기 위해서는 최대공약수로 나누어야 함

numer1, denom1, numer2, denom2 = map(int, input().split())

answer = []

#1
numer = numer1*denom2+numer2*denom1
denom = denom1*denom2

irr=[]
#2
for i in range(min(numer, denom), 0, -1) :
    if numer%i == 0 and denom%i == 0 :
        irr.append(i)

answer.append(numer//max(irr))
answer.append(denom//max(irr))

print(answer)

# if numer%2 & denom%2 == 0 :
#     numer=numer//2
#     denom=denom//2

# elif numer%3 & denom%3 == 0 :
#     numer=numer//3
#     denom=denom//3

# elif numer%5 & denom%5 == 0 :
#     numer=numer//5
#     denom=denom//5

# elif numer%7 & denom%7 == 0 :
#     numer=numer//7
#     denom=denom//7



# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     irr=[]

#     numer = numer1*denom2+numer2*denom1
#     denom = denom1*denom2

#     for i in range(min(numer, denom), 0, -1) :
#         if numer%i == 0 and denom%i == 0 :
#             irr.append(i)

#     answer.append(numer//max(irr))
#     answer.append(denom//max(irr))
    
#     return answer

# date 2023.04.22.