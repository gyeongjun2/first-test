#s1 = set([1,2,3]) 1,2열은 똑같이 집합을 만드는 방법
# s1 = {1,2,3}
# print(type(s1))

# l = [1,2,2,3,3]
# newlist = list(set(l))

# print(newlist)
s1 = set([1,2,3,4,5,6])

s1.update([7,8,9]) # update -> 집합에 새로운 수 추가
s1.remove([4,5,6]) # remove -> 집합에 있는 수 지우기
print(s1)
