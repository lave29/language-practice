# 대문자와 소문자

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 영어 대문자와 소문자로만 구성되어 있습니다.
# 입출력 예
# my_string	result
# "cccCCC"	"CCCccc"
# "abCdEfghIJ"	"ABcDeFGHij"
# 입출력 예 설명
# 입출력 예 #1

# 소문자는 대문자로 대문자는 소문자로 바꾼 "CCCccc"를 return합니다.
# 입출력 예 #2

# 소문자는 대문자로 대문자는 소문자로 바꾼 "ABcDeFGHij"를 return합니다.

# def solution(my_string):
#     answer = ''
#     return answer

# 순서도

my_string = input('my_string:')

def solution(my_string):
    answer = ''
    for i in my_string :
        if i == i.lower() :
            answer+=i.upper()
        else :
            answer+=i.lower()

    return answer

print(solution(my_string))

# 신기한게 있다 swapcase () 함수는 문자열의 대문자는 소문자로 소문자는 대문자로 바꾸어주는 함수라고 한다.
# isupper()과 islower()은 대문자인지 혹은 소문자인지 확인하는 함수라고 한다.

# date 2023.04.24.