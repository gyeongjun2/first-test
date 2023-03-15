# class 는 기본적인 틀 ex 붕어빵 만드는 틀 같은 느낌?

class Cal:
    def __init__(self):
        self.result=0

    def add(self,num):
        self.result += num
        return self.result
    
Cal1 = Cal()
Cal2 = Cal()

print(Cal1.add(3))
print(Cal1.add(4))
print(Cal2.add(3))
print(Cal2.add(4))