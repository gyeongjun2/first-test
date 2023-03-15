
from copy import copy
a = [1,2,3]

b = copy(a)
#b = a[:] #슬라이싱하면 처음부터 끝까지 a를 b에게 주는 것

a[1] = 4

print(a)
print(b)

