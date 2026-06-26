def myprint(*content):
    print(*content, end="\n\n\n")
    
### 변수
# 변수 만드는 방법 : 변수_이름 = 변수에_저장할_값
# c나 java에서는 변수를 만들떄 자료형의 타입을 직접 지정해야 함. 
# 하지만 파이썬은 변수에 저장된 값을 스스로 판단하여 자료형의 타입을 저장함.
# 파이썬에서 변수는 객체를 가리키는 것이라고도 말할 수 있음. 
# 객체는 간단히 말해 자료형의 데이터(값)와 같은 것을 의미하는 말임
# a = [1, 2, 3] 일때 [1, 2, 3]값을 가지는 리스트 데이터(객체)가 자동으로 
# 메모리에 생성되고 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소를 가르킴.

a = [1, 2, 3]
myprint(id(a)) 

# 리스트 복사하기 
# b 변수에 a 를 대입했을때 a와 b는 완전히 동일함 
# 다만 [1, 2, 3]리스트 객체를 참조하는 변수가 a,b 두개가 됨.
b = a 
myprint(id(b))
myprint(a is b)

a[1] = 4 # 리스트의 1번째 요소를 4로바꿈
myprint(a, b) 

# [:] 이용해 리스트 복제, 독립적인 복사본을 만들 수 있음
a = [1, 2, 3]
b = a[:] 
myprint(id(a), id(b)) # 주소값 다르게 나옴
myprint(a is b) # False 나옴, 둘이 다른 객체
a[1] = 4 # 리스트의 첫번쨰 요소를 4로 바꿈
myprint(a, b) # b리스트는 바뀌지 않음

# copy 모듈 이용하기 
from copy import copy
a = [1, 2, 3]
b = copy(a) # b = a[:]과 동일함
myprint(id(a), id(b))
myprint(a is b) 

# 리스트 내장 매서드 copy를 사용해도
# 모듈을 사용한 것과 동일한 결과 
c = a.copy()
myprint(c is a)

# 변수를 만드는 여러가지 방법 

# 튜플로 a, b에 값을 대입할 수 있음
a, b = ('python', 'Life') 
myprint(a, b)
(c, d) = 'python', 'Life' # 둘이 같은 예문, 튜플은 괄호를 생략해도 가능
myprint(c, d)

# 리스트로 변수를 만들 수도 있음
[e, f] = ['python', 'Life']
myprint(e, f)

# 여러개의 변수에 같은 값 대입하기 
a = b = 'python'
myprint(a, b)
myprint(id(a), id(b))
# 두 변수의 값을 바꾸기
a = 3
b = 5 
a, b = b, a
myprint(a)
myprint(b)

# a, b는 메모리가 다르게 할당되서 
# 리스트는 내용물이 수시로 추가되고 삭제될 수 있는 자료형임
# 따라서 a, b를 같은 주소에 묶어 버리면 심각한 문제 발생 
a = [1, 2, 3]
b = [1, 2, 3]
myprint(a is b) # False로 나옴



