# 외계행성의 나이

# 문제 설명
# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 
# 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
# a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 
# 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.
# 입출력 예
# age	result
# 23	"cd"
# 51	"fb"
# 100	"baa"
# 입출력 예 설명
# 입출력 예 #1

# age가 23이므로 "cd"를 return합니다.
# 입출력 예 #2

# age가 51이므로 "fb"를 return합니다.
# 입출력 예 #3

# age가 100이므로 "baa"를 return합니다.

# def solution(age):
#     answer = ''
#     return answer

# 순서도
# 1. 알파벳을 리스트로 만들기
# 2. for문으로 나이를 넣으면 그것을 바꾸면 될거같음 like 가위바위보

# 숫자를 자릿수로 나누기
# 방법1. 문자열 변환 후 나누기
# a = []
# for i in str(number):
#     a.append(i)
# 방법2. 10으로 나누어 자릿수 분리하기
# a = []
# while(number!=0):
#     a.append(number%10)
#     x = x//10
# 방법3. map 함수를 활용하기
# map(int, str(number))



alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

answer = ''

age = int(input('나이를 입력하세요:'))

for i in map(int, str(age)) :
    answer+=alphabet[i]

print(answer)




# def solution(age):
#     answer = ''
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#     for i in map(int, str(age)) :
#     answer+=alphabet[i]
#     return answer

# date 2023.04.23.


# 헐 딕셔너리 사용해도 될듯;;