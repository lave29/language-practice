# 중앙값 구하기

# 문제 설명
# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
# 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# array의 길이는 홀수입니다.
# 0 < array의 길이 < 100
# -1,000 < array의 원소 < 1,000
# 입출력 예
# array	result
# [1, 2, 7, 10, 11]	7
# [9, -1, 0]	0
# 입출력 예 설명
# 입출력 예 #1

# 본문과 동일합니다.
# 입출력 예 #2

# 9, -1, 0을 오름차순 정렬하면 -1, 0, 9이고 가장 중앙에 위치하는 값은 0입니다.

# def solution(array):
#     answer = 0
#     return answer

# 순서도
# 꼼수 : 어차피 홀수개이고 크기 순서대로 정렬되었을 때 갯수//2+1한 순서가 답 아닌가??
#        다만 순서가 0부터 시작하므로 갯수//2

array = list(map(int, input().split()))

def solution(array):
    answer = 0
    array.sort()
    answer = array[len(array)//2]
    return answer

print(solution(array))

# 다들 비슷하게 푸는구나;;
# 당연히 꼼수라고 생각했는뎁;; 핫핫;;

# date 2023.04.23.