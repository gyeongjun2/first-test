def sum(a, b):
    print("%d %d의 합은 %d입니다."%(a,b,a+b)) 

sum(1,2) # 함수에서 리턴 값이 없으면 출력이 없다는 뜻.

def sum2(c, d):
    result = c + d
    return result

print(sum2(1,2)) #리턴 값이 있으면 print

def sum_many(*args): # *args 는 모든 값을 의미 아무 값
    sum = 0
    for i in args:
        sum = sum + i
    return sum
print(sum_many(1,2,3))

def sum_and_mul(a,b):
    return a+b,a*b,a-b

print(sum_and_mul(1,2)[0])

def introduce(name, old, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
introduce("박경준",24)

A = 1
def vartest(A):
    A = A +1
    return A

A = vartest(A)
print(A)

# lambda 함수 : 함수를 편리하게 정의
myList = [lambda x, y: x+y, lambda x, y:x*y]

print(myList[0](1,2))

# input()함수
s = input("숫자를 입력하세요: ")

print(s)
