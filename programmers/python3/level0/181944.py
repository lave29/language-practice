# 홀짝 구분하기

# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd."를 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ n ≤ 1,000
# 입출력 예
# 입력 #1

# 100
# 출력 #1

# 100 is even
# 입력 #2

# 1
# 출력 #2

# 1 is odd

# a = int(input())

# 순서도
# 1. 짝수와 홀수를 구분하면 됨 → k % 2 =! 0이면 홀수, k % 2 == 0이면 짝수
# 2. 짝수이면 "n is even"을, 홀수이면 "n is odd."를 출력

#초기 작성 코드 → 문제에서는 .을 붙였지만 실제로 돌릴 때는 붙이면 안됨, input에 문장을 작성해주면 안됨;
# a = int(input('숫자를 입력해주세요:'))

# if a % 2 == 0 :
#     print("%d is even" %a)
# elif a % 2 == 1 :
#     print("%d is odd." %a)
# else :
#     print("!Error!")

#수정 코드
a = int(input('숫자를 입력해주세요:'))

if a % 2 == 0 :
    print("%d is even" %a)
elif a % 2 == 1 :
    print("%d is odd." %a)
else :
    print("!Error!")

#date 2023.04.22.