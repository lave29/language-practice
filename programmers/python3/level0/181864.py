# 문자열 바꿔서 찾기

# 문제 설명
# 문자 "A"와 "B"로 이루어진 문자열 myString과 pat가 주어집니다. 
# myString의 "A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 pat이 있으면 1을 아니면 0을 return 하는 solution 함수를 완성하세요.

# 제한사항
# 1 ≤ myString ≤ 100
# 1 ≤ pat ≤ 10
# myString과 pat는 문자 "A"와 "B"로만 이루어진 문자열입니다.
# 입출력 예
# myString	pat	result
# "ABBAA"	"AABB"	1
# "ABAB"	"ABAB"	0
# 입출력 예 설명
# 입출력 예 #1

# "ABBAA"에서 "A"와 "B"를 서로 바꾸면 "BAABB"입니다. 여기에는 부분문자열 "AABB"가 있기 때문에 1을 return 합니다.
# 입출력 예 #2

# "ABAB"에서 "A"와 "B"를 서로 바꾸면 "BABA"입니다. 여기에는 부분문자열 "BABA"가 없기 때문에 0을 return 합니다.

# def solution(myString, pat):
#     answer = 0
#     return answer

# 순서도
# 1. for 로 myString을 하나씩 넣고 이때, if i==A 일 경우 B를 elif i==B 일 경우 A를
# 2. A.count(pat)을 통해 true라면 1을 false라면 0을 출력하도록 하였음

myString = input('myString:')
pat = input('pat:')

def solution(myString, pat):
    answer = 0
    temp = ''
    for i in myString :
        if i == 'A' :
            temp += 'B'
        elif i == 'B' :
            temp += 'A'

    if temp.count(pat) :
        answer = 1
    else :
        answer = 0
    return answer

print(solution(myString, pat))


# date 2023.05.03.