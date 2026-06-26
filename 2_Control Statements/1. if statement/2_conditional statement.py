def myprint(*data):
    print(*data, end="\n\n\n")

### 조건문 (conditional statement)
# if 조건문에서 '조건문'이란 참과 거짓을 판단하는 문장을 말함

# 비교 연산자
# X<Y : X가 Y보다 작다.
# X>Y : X가 Y보다 크다.
# X == Y : X가 Y가 같다.
# X != Y : X와 Y가 같지 않다.
# X >= Y : X가 Y보다 크거나 같다.
# X <= Y : X가 Y보다 작거나 같다.
x = 3
y = 2
myprint(x > y)
myprint(x < y)
myprint(x == y)
myprint(x != y)
# 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
if money >= 3000:
    myprint("택시를 타고 가라")
else :
    myprint("걸어가라")
# 돈이 2000원 이므로 '걸어가라' 출력


# and, or, not
# x or y : x와 y 둘 중 하나만 참이어도 참이다.
# x and y : x와 y 모두 참이어야 참이다.
# not x : x가 거짓이면 참이다. 
# 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    myprint("택시를 타고 가라")
else:
    myprint("걸어가라")
# money는 2000원이지만, card가 True이기 때문에 조건문이 참이된다.


# in, not in
# x in 리스트 / x not in 리스트
# x in 튜플 / x not in 튜플
# x in 문자열 / x not in 문자열 
# True와 False 값을 리턴함 
myprint(1 in [1, 2, 3]) 
myprint(1 not in [1, 2, 3])
myprint('a' in ('a', 'b', 'c'))
myprint('j' in 'python')
# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
poket = ['paper', 'cellphone', 'money']
if 'money' in poket:
    myprint("택시를 타고 가라")
else:
    myprint("걸어가라")
# 'money'가 poket에 있으므로 '택시를 타고 가라' 출력

# 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라
poket = ['paper', 'cellphone', 'money']
if 'card' not in poket:
    myprint("걸어가라")
else:
    myprint("택시를 타고 가라")
    
    
# 조건문에서 아무일도 하지 않게 설정하기 
# 주머나에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
poket = ['paper', 'cellphone', 'money']
if 'money' in poket:
    pass
else:
    myprint("카드를 꺼내라")
# pass를 사용하면 아무 일도 하지 않음






