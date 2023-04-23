# 배열 원소의 길이

# 문제 설명
# 문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ strlist 원소의 길이 ≤ 100
# strlist는 알파벳 소문자, 대문자, 특수문자로 구성되어 있습니다.
# 입출력 예
# strlist	result
# ["We", "are", "the", "world!"]	[2, 3, 3, 6]
# ["I", "Love", "Programmers."]	[1, 4, 12]
# 입출력 예 설명
# 입출력 예 #1

# ["We", "are", "the", "world!"]의 각 원소의 길이인 [2, 3, 3, 6]을 return합니다.
# 입출력 예 #2

# ["I", "Love", "Programmers."]의 각 원소의 길이인 [1, 4, 12]을 return합니다.

# def solution(strlist):
#     answer = []
#     return answer

# 순서도
# 1. for문으로 매개변수가 나오게 한다
# 2. len()으로 길이를 담는다
# 3. append()로 return할 배열을 만든다

strlist = ["We", "are", "the", "world!"]

answer = []

for i in strlist :
    answer.append(len(i))

print(answer)



def solution(strlist):
    answer = []
    for i in strlist :
        answer.append(len(i))
    return answer

#date 2023.04.23.