# 가위 바위 보

# 문제 설명
# 가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때,
# rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < rsp의 길이 ≤ 100
# rsp와 길이가 같은 문자열을 return 합니다.
# rsp는 숫자 0, 2, 5로 이루어져 있습니다.
# 입출력 예
# rsp	result
# "2"	"0"
# "205"	"052"
# 입출력 예 설명
# 입출력 예 #1

# "2"는 가위이므로 바위를 나타내는 "0"을 return 합니다.
# 입출력 예 #2

# "205"는 순서대로 가위, 바위, 보이고 이를 모두 이기려면 바위, 보, 가위를 순서대로 내야하므로 “052”를 return합니다.

# def solution(rsp):
#     answer = ''
#     return answer

# 순서도
# 1. 가위는 2, 바위는 0, 보는 5이다.
# 2. 가위바위보는 6가지의 경우의 수가 있다

# 가위=가위
# 바위=바위
# 보=보
# 가위=바위
# 가위=보
# 바위=보

# 이기려면 rsp가 가위일 경우에는 바위를
# 바위일 경우에느 보를
# 보일 경우에는 가위를 내야한다

# 3. 따라서 이럴 경우에는 if문을 사용하면 될 것 같다.
# if rsp=="가위"
#     바위
# elif rsp=="바위"
#     보
# elif rsp=="보"
#     가위
# 라고 생각했는데 틀린 것 같음;;

###############################################################################
# if '가위' in rsp
#가위2s 바위0r 보5p
import re


#answer = ""

#k = list(rsp)

#print(k)


# print(len(rsp))
# P=rsp.find('5')
# R=rsp.find('0')
# S=rsp.find('2')
# print(P, R, S)

# for P in re.finditer("5", rsp) :
#     print(P.start())

# for R in re.finditer("0", rsp) :
#     print(P.start())

# for S in re.finditer("2", rsp) :
#     print(P.start())
# #가위
# if 2 in rsp :
#     #print(rsp.index(2))
#     answer = 0
# else :
#     answer = 4

# print(answer)
# #바위
# elif 0 in day :
#     answer = 5
# #보
# elif 5 in day :
#     answer = 2
# i = 0
# for i in rsp :
#     print(i)

# day=[1, 2, 3, 'MON', 'TUE', 'WED']

# if 'MON' in day :
#     print('True')
# else :
#     print('False')

# for i in day :
#     print(i)

# # #0~9
# # for i in range(10) :
# #     print(i)

# # #3~9
# # for i in range(3, 10) :
# #     print(i, end='')    #이어지는법

# # for i in range(0, 10, 2) :
# #     print(i)

# for i in 'string' :
#     print(i, end='')

rsp = input("가위(2), 바위(0), 보(5)를 숫자로 입력하세요:")

answer = ""

for i in rsp :
    if i=='2' :
        answer+='0'
    elif i=='0' :
        answer+='5'
    elif i=='5' :
        answer+='2'

print(answer)



# def solution(rsp):
    
#     answer = ''
    
#     for i in rsp :
#         if i=='2' :
#             answer+='0'
#         elif i=='0' :
#             answer+='5'
#         elif i=='5' :
#             answer+='2'
    
#     return answer

#date 2023.04.23.
#19일 첫번째 시도 실패 이후 23일 두번째 시도에 드디어 성공!!
#공부가 필요하다...;;