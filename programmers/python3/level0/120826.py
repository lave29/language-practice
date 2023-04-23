# 특정 문자 제거하기

# 문제 설명
# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# letter은 길이가 1인 영문자입니다.
# my_string과 letter은 알파벳 대소문자로 이루어져 있습니다.
# 대문자와 소문자를 구분합니다.
# 입출력 예
# my_string	letter	result
# "abcdef"	"f"	"abcde"
# "BCBdbe"	"B"	"Cdbe"
# 입출력 예 설명
# 입출력 예 #1

# "abcdef" 에서 "f"를 제거한 "abcde"를 return합니다.
# 입출력 예 #2

# "BCBdbe" 에서 "B"를 모두 제거한 "Cdbe"를 return합니다.

# def solution(my_string, letter):
#     answer = ''
#     return answer

# 순서도
# remove로 삭제라고 생각했으나 이건 리스트가 아님
# level0의 쉬운 문제라고 생각하고 가볍게 다시 문제를 읽어보면
# letter은 1인 영문자 따라서 for문으로 my_string을 나열하면서 letter가 아닌 것들만 합쳐주면 됨

my_string = input('my_string:')
letter = input('letter:')

answer = ''

for i in my_string :
    if i!= letter :
        answer+=i

print(answer)



# def solution(my_string, letter):
#     answer = ''
#     for i in my_string :
#         if i!= letter :
#             answer+=i
#     return answer

# 대박....그냥 replace로 해도 되는구나;;

# my_string = input('my_string:')
# letter = input('letter:')

# answer = ''

# answer = my_string.replace(letter, '')

# print(answer)

#date 2023.04.23.