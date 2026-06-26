def myprint(content):
    print(content, end="\n\n\n")
    
### 잡합 자료형
# 집합 자료형 만들기 
s1 = set([1, 2, 3])
myprint(s1)
s2 = set("Hello")
myprint(s2)

# 집합 자료형의 특징
# 1. 증복을 허용하지 않음
# 2. 순서가 없음 
# 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 요소를 얻을 수 있지만 
# set 자료형은 순서가 없기 때문에 인덱싱을 통해 요소값을 얻을 수 없다
# 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 해야 한다.
s1 = set([1, 2, 3])
l1 = list(s1) # s1을 리스트로 변환
myprint(l1)
myprint(l1[0])
t1 = tuple(s1) # s1을 튜플로 변환
myprint(t1)
myprint(t1[0])