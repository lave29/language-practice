# 문자 반복 출력하기

# 문제 설명
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, 
# my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 2 ≤ my_string 길이 ≤ 5
# 2 ≤ n ≤ 10
# "my_string"은 영어 대소문자로 이루어져 있습니다.
# 입출력 예
# my_string	n	result
# "hello"	3	"hhheeellllllooo"
# 입출력 예 설명
# 입출력 예 #1

# "hello"의 각 문자를 세 번씩 반복한 "hhheeellllllooo"를 return 합니다.

# def solution(my_string, n):
#     answer = ''
#     return answer

# 순서도
# for문으로 my_string을 하나씩 나오게 하고 *n을 해서 붙여주면 됨

my_string = input('문자열:')
n = int(input('정수:'))

answer = ''

for i in my_string :
    answer += i*n
    
print(answer)



def solution(my_string, n):
    answer = ''
    for i in my_string :
        answer += i*n
    return answer

#date 2023.04.23.

# 내포된 for문 할 때 []는 리스트라서 안될 줄 알았는데;; 바부당;;
# ''.join(i*n for i in my_string)
