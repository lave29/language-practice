# 점의 위치 구하기

# 문제 설명
# 사분면은 한 평면을 x축과 y축을 기준으로 나눈 네 부분입니다. 사분면은 아래와 같이 1부터 4까지 번호를매깁니다.

# 스크린샷 2022-07-07 오후 3.27.04 복사본.png

# x 좌표와 y 좌표가 모두 양수이면 제1사분면에 속합니다.
# x 좌표가 음수, y 좌표가 양수이면 제2사분면에 속합니다.
# x 좌표와 y 좌표가 모두 음수이면 제3사분면에 속합니다.
# x 좌표가 양수, y 좌표가 음수이면 제4사분면에 속합니다.
# x 좌표 (x, y)를 차례대로 담은 정수 배열 dot이 매개변수로 주어집니다. 좌표 dot이 사분면 중 어디에 속하는지 1, 2, 3, 4 중 하나를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# dot의 길이 = 2
# dot[0]은 x좌표를, dot[1]은 y좌표를 나타냅니다
# -500 ≤ dot의 원소 ≤ 500
# dot의 원소는 0이 아닙니다.
# 입출력 예
# dot	result
# [2, 4]	1
# [-7, 9]	2
# 입출력 예 설명
# 입출력 예 #1

# dot이 [2, 4]로 x 좌표와 y 좌표 모두 양수이므로 제 1 사분면에 속합니다. 따라서 1을 return 합니다.
# 입출력 예 #2

# dot이 [-7, 9]로 x 좌표가 음수, y 좌표가 양수이므로 제 2 사분면에 속합니다. 따라서 2를 return 합니다.

# def solution(dot):
#     answer = 0
#     return answer

# 순서도
# 1. if문으로 x>0 and y>0 1사분면, x<0 and y>0 2사분면, x<0 and y<0 3사분면, x>0 and y<0 4사분면




dot = list(map(int, input().split()))

answer=0

if dot[0]>0 and dot[1]>0 :
    answer = 1
elif dot[0]<0 and dot[1]>0 :
    answer = 2
elif dot[0]<0 and dot[1]<0 :
    answer = 3
elif dot[0]>0 and dot[1]<0 :
    answer = 4
else :
    answer = "Error"

print(answer)




def solution(dot):
    answer = 0
    
    if dot[0]>0 and dot[1]>0 :
        answer = 1
    elif dot[0]<0 and dot[1]>0 :
        answer = 2
    elif dot[0]<0 and dot[1]<0 :
        answer = 3
    elif dot[0]>0 and dot[1]<0 :
        answer = 4
    else :
        answer = "Error"
    
    return answer

# date 2023.04.23.