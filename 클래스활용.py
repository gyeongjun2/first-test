class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second): #self 는
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first + self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    def mul(self):
        result = self.first / self.second
        return result

class MoreFourcal(Fourcal): #자식 클래스, 클래스의 상속 부모 클래스의 모든 기능 사용 가능
    def pow(self):
        result = self.first ** self.second
        return result
class MoreFourcal2(Fourcal):
    def div(self):
        if (self.second == 0):
            return 0
        else:
            return self.first / self.second    

a = MoreFourcal(8,2)
b = MoreFourcal2(12,2)
print(b.div())

class Family:
    lastname = "김"

Family.lastname = "박" #Family 클래스 설계도 자체를 호출해서 변수를 바꿀 수 있다.
print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

from mod1 import add
print(add(1,2))


    
