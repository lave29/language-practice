# 암호 해독

# 문제 설명
# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.

# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ cipher의 길이 ≤ 1,000
# 1 ≤ code ≤ cipher의 길이
# cipher는 소문자와 공백으로만 구성되어 있습니다.
# 공백도 하나의 문자로 취급합니다.
# 입출력 예
# cipher	code	result
# "dfjardstddetckdaccccdegk"	4	"attack"
# "pfqallllabwaoclk"	2	"fallback"
# 입출력 예 설명
# 입출력 예 #1

# "dfjardstddetckdaccccdegk" 의 4번째, 8번째, 12번째, 16번째, 20번째, 24번째 글자를 합친 "attack"을 return합니다.
# 입출력 예 #2

# "pfqallllabwaoclk" 의 2번째, 4번째, 6번째, 8번째, 10번째, 12번째, 14번째, 16번째 글자를 합친 "fallback"을 return합니다.

# def solution(cipher, code):
#     answer = ''
#     return answer

# 순서도
# 1. for i in range(code, len(cipher)+1, code)를 하면 배수 번째 글자만 특정할 수 있다
# 2. cipher을 리스트로 바꾸어서 꺼내면 되지 않을까??
# 결론 : 라고 생각했는데 string[start:end:step]이 있었네;;;

cipher = input('문자열 cipher:')
code = int(input('정수 code:'))

def solution(cipher, code):
    answer = ''
    answer = cipher[code-1:len(cipher)+1:code]
        
    return answer

print(solution(cipher, code))

# 이번에 조금 잘 풀은듯? ㅋㅋㅋ


# date 2023.04.24.