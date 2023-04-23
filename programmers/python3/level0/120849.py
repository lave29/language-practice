# 모음 제거

# 문제 설명
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# my_string은 소문자와 공백으로 이루어져 있습니다.
# 1 ≤ my_string의 길이 ≤ 1,000
# 입출력 예
# my_string	result
# "bus"	"bs"
# "nice to meet you"	"nc t mt y"
# 입출력 예 설명
# 입출력 예 #1

# "bus"에서 모음 u를 제거한 "bs"를 return합니다.
# 입출력 예 #1

# "nice to meet you"에서 모음 i, o, e, u를 모두 제거한 "nc t mt y"를 return합니다.

# def solution(my_string):
#     answer = ''
#     return answer

# 순서도
# 1. for문에 my_string을 넣음
# 2. if로 모음이 아닌 경우 answer에 들어가도록 함

my_string = input('문자열:')

def solution(my_string):
    answer = ''
    
    for i in my_string :
        if i!='a' and i!='e' and i!='i' and i!='o' and i!='u' :
            answer += i
    return answer

print(solution(my_string))

#sub, replace, "".join([i for i in my_string if not(i in "aeiou")]) 등 다양한 방법이 있네;

#date 2023.04.23.