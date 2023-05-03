# 문자열 섞기

# 문제 설명
# 길이가 같은 두 문자열 str1과 str2가 주어집니다.

# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ str1의 길이 = str2의 길이 ≤ 10
# str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.
# 입출력 예
# str1	str2	result
# "aaaaa"	"bbbbb"	"ababababab"

# def solution(str1, str2):
#     answer = ''
#     return answer

# 순서도
# 1. 문자열인 str1과 str2를 list로 바꾼다
# 2. str1의 길이와 str2의 길이가 같으므로 for를 이용하여 list 갯수만큼 나오게 하여 answer에 str1과 str2가 골고루 들어가게 함

# str1 = input('문자열 str1:')
# str2 = input('문자열 str2:')

# def solution(str1, str2):
#     answer = ''
#     str1=list(str1)
#     str2=list(str2)
#     for i in range(0, len(str1)) :
#         answer += str1[i]+str2[i]
#     return answer

# print(solution(str1, str2))

# 파이썬의 경우 특정 위치의 문자열을 list화 시키지 않아도 나타낼 수 있음;;;

str1 = input('문자열 str1:')
str2 = input('문자열 str2:')

def solution(str1, str2):
    answer = ''
    for i in range(0, len(str1)) :
        answer += str1[i]+str2[i]
    return answer

print(solution(str1, str2))

# date 2023.05.03.