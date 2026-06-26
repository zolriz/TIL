def myprint(*data):
    print(*data, end='\n\n\n')
    
### 클래스 ### 
# 클래스는 쉽게 말해 '무언가를 똑같이 찍어내기 위한 툴' 또는 '설계도'라고 생각하면 이해하기 쉬움
# 클래스 = 설계도 : 종이에 그려진 건물의 설계도 그 자체. 설계도 자체는 가상의 도면일 뿐, 들어가 살순 없음
# 객체/인스턴스 = 실제 건물 : 설계도를 보고 콘크리트를 부어 실제로 지은 건물

# 클래스는 왜 필요한가?
# 클래스가 없어도 충분히 프로그램을 만들 수는 있음
# 하지만 프로그램을 작성할때 클래스를 적재적소에 사용하면 프로그래머가 얻을 수 있는 이익은 많음

# 계산기 프로그램을 만들며 클래스 클래스 알아보기 
result = 0
def add(num):
    global result
    result += num # 결괏값(result)에 입략값(num) 더하기
    return result # 결괏값 리턴 
print(add(3))
myprint(add(4))
# 입략값을 이전에 계산한 결괏값에 더한 후 리턴하는 add 함수를 적성
# 이전에 계산한 결괏값을 유지하기 위해서 result 전역 변수(global)를 사용함

# 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야할까?
# 계산기는 각각의 결괏값을 유지해야 하므로 add 함수 하나로는 
# 따라서 계산기를 각각 따로 만들어야함
result1 = 0
result2 = 0
def add1(num): # 계산기 1
    global result1
    result1 += num
    return result1 
def add2(num): # 계산기 2
    global result2
    result2 += num
    return result2
print(add1(3))
print(add1(4))
print(add2(3))
myprint(add2(7))
# 계산기 1의 결괏값이 계산기 2에 아무런 영향을 끼치지 못한다는것을 확인
# 하지만 계산기가 더 늘어난다면 어떻게 해야할까?
# 클래스를 사용하면 간단히 해결할 수 있음
class Calculator:
    def __init__(self): # __init__ 클래스로 객체를 생성할때 그 객체가 기본적으로 가지고 있는 초기 상태, self : 현재 작동하고있는 계산기 내부
        self.result = 0 # self.result : 다른 계산기 말고, 지금 만들어진 '이 계산기의 result 상자를 0으로 세팅 해라 라는 뜻
    def add(self, num): 
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
myprint(cal2.add(7))
# calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 '객체' 리거 부름)가 각각의 역활을 수행

# 빼기 기능 추가
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.result += num
        return self.result
    
    def sub(self, num):
        self.result -= num
        return self.result 



## 클래스와 객체 
# 클래스란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀)
# 객체란 클래스로 만든 피조물(과자 틀로 찍어낸 과자)
# 클래스로 만든 객체는 독립적임(서로 영향x)
class Cookie:
    pass
# 아무런 기능이 없는 클래스 하지만 객체는 무수히 생성 가능 
a = Cookie()
b = Cookie()
# Cookie()의 결괏값을 리턴받은 a와 b가 바로 객체임
# 클래스로 만든 갤체를 '인스턴스'라고 함 a = Cookie()에서 'a는 객체 이다', 'a는 Cookie의 인스턴스 이다'


## 사칙연산 클래스 만들기
# 1) 클래스를 어떻게 만들지 구상하기
# 사칙 연산 클래스 FourCal/두 숫자를 입력 받는 setdata/더하기 기능인 add/곱하기 기능인 mul/빼기 기능인 sub/나누기 기능인 div
 
 
# 2) 클래스 구조 만들기
class FourCal:
    pass # 아무런 기능이 없는 클래스, 객체는 생성 가능

a = FourCal() 
myprint(type(a)) # <이 객체의 성격, 현재 실행 중인 파일의 이름, 클래스의 이름>


# 3) 객체에 연산할 숫자 지정하기
class FourCal:
    def setdata(self, first, second): # 메서드의 매개변수
        self.first = first # self(객체)(a)의 first상자에 4(first)대입
        self.second = second # self(객체)(a)의 second상자에 2(second)대입
# FourClass에서 setdata 함수를 정의, 클래스 안에 구현된 함수는 다른말로 메서드(method)라고 부름
a = FourCal()
a.setdata(4, 2)
# setdata 메서드에는 self, first, second 총 3개의 매개변수가 필요한데 실제로는 2개의 값만 전달
# 매서드의 첫번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 들어감
# FourCal.setdata(a, first, second) 형태로 번역함
myprint(a.first)
myprint(a.second)
# a, b 객체 만들기
a = FourCal()
b = FourCal()
a.setdata(4,2) # a 객체에 객체변수 first와 second가 생성되고 값 4와 2 대입
myprint(a.first) # a 객체의 first 값 출력
b.setdata(3,7) # b 객체에 객체변수 first와 second가 생성돠고 값 3과 7 대입
myprint(b.first) # b 객체의 first 값 출력
myprint(a.first) # a 객체는 b 객체의 영행을 받지 않고 원래 값을 유지


# 4) 더하기 기능 만들기
# FourCal()에 add 매서드 만들면 됨
class FourCal:
    def setdata(self, first, second): 
        self.first = first 
        self.second = second 
    def add(self):
        result = self.first + self.second
        return result
    
a = FourCal()
a.setdata(4, 2)
myprint(a.add()) # result = a.first + a.second = 4 + 2


# 5) 곱하기, 빼기, 나누기 만들기
class FourCal():
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
    
a = FourCal()
a.setdata(4, 2)
myprint(a.add(), a.sub(), a.mul(), a.div()) # ()를 붙이는 이유 : 이 메서드를 실행하라는 파이썬 문법적 약속
                                            # ()비워두는 이유 : 이미 .앞의 객체가 self로 들어갔고, 추가로 전달할 매개변수 가 없기 때문



## 생성자 
# FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 먼저 수행하면 오류가 발생
# setdata 메서드를 수행해야 객체 a의 객체변수 first와 second가 생성되기 때문임
# 이럴때는 생성자를 구현하는게 안전한 방법임
# 생성자란 객체가 생성될 떄 자동으로 호출되는 메서드를 의미함, 파이썬 메서드 명으로 __init__를 사용하면 이 메서드는 생성자가 됨

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first*self.second
        return result
    def div(self):
        result = self.first/self.second
        return result
# __init__ 메서드는 setdata 메서드와 이름만 다르고 모든게 동일함
# 단, 메서드 이름을 __init__로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출됨
# a = Fourcal()을 수행할 때 생성자 __init__ 가 호출되어 위와 같은 오류 발생
# 오류 발샐 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문

a = FourCal(4, 2) # self : 생성되는 객체, first : 4, second : 2
myprint(a.first)
myprint(a.second)
myprint(a.add())
myprint(a.div())



## 클래스의 상속
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
# class 클래스_이름(상속할_클래스_이름)
class MoreFourCal(FourCal):
    pass
#  MoreFourCal 클래스는 FourCal 클래스를 상속했으므로 FourCal 클래스의 모든 기능을 사용할 수 있음
a = MoreFourCal(4, 2)
myprint(a.add(), a.mul(), a.sub(), a.div())
# a^b를 계산하는 MoreFourCal 클래스 만들기
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first**self.second # 제곱연산자 **
        return result
a = MoreFourCal(4, 2)
myprint(a.pow())



## 매서드 오버라이딩 
# a = FourCal(4, 0)
# a.div() 4를 0으로 나누려고 해서 ZeroDivisionError 오류가 발생 
# 0으로 나눌때 오류가 아닌 값 0을 리턴 받는법 

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first/self.second
# FourCal 클래스에 있는 div 메서드를 동일한 이름으로 다시 작성 
# 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩 이라고 함
a = SafeFourCal(4, 0)
myprint(a.div())



## 클래스 변수
# 클래스안에 변수를 선언하여 생성
# 클래스_이름.클래스변수로 사용가능
# 클래스 변수는 객체변수와 달리 모든 객체에 공유됨
class Family:
    lastname = "김"
a = Family()
b = Family()
myprint(a.lastname)
myprint(b.lastname)

    
    


 

