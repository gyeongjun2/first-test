# test_list = ['one', 'two','three']

# for i in test_list: #리스트나 튜플에 있는 변수를 i에 하나씩 빼와서 출력
#         print(i)
# #########################
# a = [(1,2), (3,4),(5,6)]
# for (first, last) in a:
#         print(first)
#         print(last)
# #########################
#
# marks = [90, 25, 67, 45, 80]
# number = 0

# for mark in marks:
#     number = number + 1
#     if mark < 60: continue
#     print("%d번 학생은 합격입니다." %number)
# ###########################
# range 함수로 숫자 합 구하기
# sum = 0
# for i in range(1, 11):
#     sum = sum + i
#     print(sum)
# ##########################

# 2중 for문
a = 10
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')
