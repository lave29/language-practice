# 3. 두개의 리스트를 입력 받아 A-B를 빼는 프로그램을 구현하세요. (4점)
# – array_diff(A,B) 함수
# • 예
# array_diff([1,2],[1]) 
# • 여기서 list A=[1,2]이고, list B=[1]이다. 
# • A-B를 통해 반환 [2]를 반환한다. 
# array_diff([1,2,2,2,3],[2]) 일 때 반환 값 [1,3]
# array_diff([1,2,2], [1]) 일 때 반환 값 [2,2] 
# array_diff([1,2,2], []) 일 때 반환 값 [1,2,2]
# array_diff([], [1,2]) 일 때 반환 값 []

A = list(map(int, input('A:').split()))
B = list(map(int, input('B:').split()))

def array_diff(A, B):
    for i in B :
        while i in A :
            A.remove(i)

    return A

print(array_diff(A, B))



# def array_diff(A, B):
#     # for i in B :
#     #     # print(type(i))
#     #     if i in A :
#     #         A.remove(i)

#     # answer = []
#     for i in B :
#         # if i not in A :
#         #     answer.append(i)
#         while i in A :
#             A.remove(i)

#     return A


# # 허유진
# def array_diff(A, B):
#     an = []
#     for i in A :
#         for a in B :
#             if i!=a :
#                 an.append(i)
#     return an