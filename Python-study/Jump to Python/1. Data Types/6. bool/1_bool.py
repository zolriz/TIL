def myprint(content):
    print(content, end="\n\n\n")
    
### 불 자료형 
# 불 자료형은 참(true)과 거짓(false)을 나타내는 자료형이다 
# 불 자료형은 True 와 False 값만 가질 수 있다. (True나 False는 파이썬의 예약어로, 첫 문자를 항상 대문자로 작성해야함)


# 불 자료형 사용법 
a = True
b = False 
myprint(type(a)) # type(x) 는 x의 자료형을 확인하는 파이썬의 내장 함수이다.
myprint(type(b))

# 볼 자료형은 조건문의 리턴값으로 사용됨
myprint(1==1) # 1과 1이 같은가?
myprint(2>1)  # 2가 1보다 큰가?
myprint(2<1)  # 2가 1보다 작은가?




