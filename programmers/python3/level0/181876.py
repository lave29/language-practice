# 소문자로 바꾸기

# 문제 설명
# 알파벳으로 이루어진 문자열 myString이 주어집니다. 모든 알파벳을 소문자로 변환하여 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ myString의 길이 ≤ 100,000
# myString은 알파벳으로 이루어진 문자열입니다.
# 입출력 예
# myString	result
# "aBcDeFg"	"abcdefg"
# "aaa"	"aaa"

# def solution(myString):
#     answer = ''
#     answer = myString.lower()
#     return answer

# 순서도
# 전부 소문자로 변환하는 것이므로 str.lower()을 사용하여 변환하기




myString = input('myString:')

def solution(myString):
    answer = ''
    answer = myString.lower()
    return answer

print(solution(myString))



# date 2023.04.24.