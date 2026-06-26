def myprint(content):
    print(content, end = "\n\n\n")

### 자료형의 참과 거짓 
# "python" --- 참
# "" --- 거짓
# [1, 2, 3] --- 참
# [] --- 거짓
# (1, 2, 3) --- 참
# () --- 거짓
# {'a': 1} --- 참
# {} --- 거짓
# 1 --- 참
# 0 --- 거짓
# None --- 거짓
# 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓이 되고 비어 있지 않으면 참이 됨 
# 숫자는 그 값이 0일 때 거짓이 됨, None도 거짓

a = [1, 2, 3, 4]
while a: # a가 참인 동안
    myprint(a.pop()) # 리스트의 마지막 요소를 하나씩 꺼냄
    # 리스트 안에 요소가 존재하는 한(a가 참인 동안) 마지막 요소를 계속 끄집어내고,
    # 결국 더 이산 끄집어 낼 것이 없으면 a가 빈 리스트가 되어 거짓이 됨.
    
if []: # 만약 []가 참이면 
    myprint("참")
else: # 만약 []가 거짓이면
    myprint("거짓") 
    
# 불 연산 - 불 함수를 이용해 자료형의 참과 거짓 확인가능
myprint(bool('python'))
myprint(bool(''))
myprint(bool([1, 2, 3]))
myprint(bool([]))
myprint(bool(0))
myprint(bool(3))

a = [1, 2, 3]
myprint(id(a))
