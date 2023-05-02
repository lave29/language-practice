# 팩토리얼

# 문제 설명
# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
#        예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
#        정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 return 하도록 solution 함수를 완성해주세요.

# i! ≤ n
# 제한사항
# 0 < n ≤ 3,628,800
# 입출력 예
# n	result
# 3628800	10
# 7	3
# 입출력 예 설명
# 입출력 예 #1

# 10! = 3,628,800입니다. n이 3628800이므로 최대 팩토리얼인 10을 return 합니다.
# 입출력 예 #2

# 3! = 6, 4! = 24입니다. n이 7이므로, 7 이하의 최대 팩토리얼인 3을 return 합니다.

# def solution(n):
#     answer = 0
#     return answer

# 순서도
# 1. n은 정수, i! 팩토리얼 계산된 값
# 2. ex) 5 = 5*4*3*2*1 따라서 어떤 순서로든 나와서 곱하면 됨
# 3. but, 팩토리얼 계산 된 n으로 팩토리얼 i!의 i 값을 찾는 것임
# 4. 따라서 1부터 n까지 숫자를 곱하면서 곱한 값이 n이 될 경우 멈추고 마지막으로 곱한 값 i가 우리가 찾는 i가 되는 것

n = int(input('팩토리얼할 정수 n을 입력하세요:'))

def solution(n):
    answer = 1
    for i in range(1, n+1) :
        answer *= i
        if answer >= n :
            if answer == n :
                answer = i
            elif answer > n :
                answer = i - 1
            break
    return answer

print(solution(n))

# date 2023.05.02.