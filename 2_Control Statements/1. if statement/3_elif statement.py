def myprint(*data):
    print(*data, end="\n\n\n")

### elif 문 
# if 와 else 만으로는 다양한 조건을 판단하기는 어려움
# 다중조건을 판단할때 elif 사용 (else + if)
# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만
# 카드가 있으면 택시를 타고 가고, 돈도 없고, 카드도 없으면 걸어가라.
poket = ['paper', 'cellphone']
card = True
if 'money' in poket:
    myprint("택시를 타고 가라")
else:
    if card:
        myprint("택시를 타고 가라")
    else:
        myprint("걸어가라")
# elif 시용시
poket = ['paper', 'cellphone']
card = True
if 'money' in poket:
    myprint("택시를 타고 가라")
elif card:
    myprint("택시를 타고 가라")
else:
    myprint("걸어가라")
# 즉, elif는 이전 조건문이 거짓일 때 수행됨


# if elif, else 사용시 구조
# if 조건문:
#    수행할_문장1
#    수행할_문장2
#    ...
# elif 조건문:
#   수행할_문장1
#   수행할_문장2
#   ...
# elif 조건문:
#   수행할_문장1
#   수행할_문장2
#   ...
#   (...생략...)
# else:
#   수행할_문장1
#   수행할_문장2
#   ...
#   ...
# elif는 개수에 제한 없이 사용가능


# if 문을 한 줄로 작성하기 
poket = ['paper', 'money', 'cellphone']
if 'money' in poket: pass
else: myprint("카드를 꺼내라")
# if, else문 다음에 수행할 문장을 콜론(:) 뒤에 바로 적음


# 조건부 표현식
# 변수 = 조건문이 참인 경우의 값 if 조건문 else 조건문이 거짓인 경우의 값
# score가 60 이상일 경우 message에 문자열"success", 아닐 경우에는 문자열 "faile" 대입
score = 70
if score >= 60:
    message = "sussess"
else:
    message = "failure"
myprint(message)
# 조건부 표현식을 사용해 한 줄로 작성하기 
message = "success" if score >= 80 else "failure"
myprint(message)


  

    



    