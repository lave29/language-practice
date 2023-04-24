# 문자열안에 문자열

# 문제 설명
# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ str1의 길이 ≤ 100
# 1 ≤ str2의 길이 ≤ 100
# 문자열은 알파벳 대문자, 소문자, 숫자로 구성되어 있습니다.
# 입출력 예
# str1	str2	result
# "ab6CDE443fgh22iJKlmn1o"	"6CD"	1
# "ppprrrogrammers"	"pppp"	2
# "AbcAbcA"	"AAA"	2
# 입출력 예 설명
# 입출력 예 #1

# "ab6CDE443fgh22iJKlmn1o" str1에 str2가 존재하므로 1을 return합니다.
# 입출력 예 #2

# "ppprrrogrammers" str1에 str2가 없으므로 2를 return합니다.
# 입출력 예 #3

# "AbcAbcA" str1에 str2가 없으므로 2를 return합니다.

# def solution(str1, str2):
#     answer = 0
#     return answer

# 순서도
# for문에서 str1과 str2를 나오게하고 if로 유무를 확인하고 존재하면 1을, 존재하지 않으면 2를 return 하면 될거라고 생각했음
# 문제를 잘못읽었어;;;
# str1.find(str2)를 해서 -1이 나오면 맞는게 없으므로 2를, 그 외의 숫자가 나오면 find가 된 것이 있으므로 1을

str1 = input('str1:')
str2 = input('str2:')

def solution(str1, str2):
    answer = 0

    if str1.find(str2) == -1 :
        answer = 2
    else :
        answer = 1

    return answer

print(solution(str1, str2))



#return 1 if str2 in str1 else 2
# 이렇게 간단히 된다니;;
# 역시 나는 if문을 아직 잘 모르는거 같음ㅠ

# date 2023.04.24.