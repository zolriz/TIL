### 매서드 함수 차이
# 함수는 독립적인 도구이고, 매서드는 객체 전용도구 이다

def myprint(content):
    print(content, end ="\n\n\n")
    
### 집합 자료형 관련 함수 

# 1. add - 값 1개 추가하기
s1 = set([1, 2, 3])
myprint(s1.add(4))
myprint(s1)

# 2. update - 값 여러개 추가하기 
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
myprint(s1)

# 3. remove - 특정 값 제거하기 
s1 = set([1, 2, 3])
s1.remove(2)
myprint(s1)