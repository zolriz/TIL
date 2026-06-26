def myprint(*data):
    print(*data, end="\n\n\n")
    
### while 문
# while 문은 반복문의 한 종류
# 문장을 반복해서 수행해야 할 경우 while 문을 사용함

# while 문의 기본 구조
# while 조건문:
#   수행할_문장1
#   수행할_문장2
#   수행할_문장3
#   ...
# while 문은 조건문이 참인 동안 while 문에 속한 문장들이 반복해서 수행됨.

# 열 번 찍어 안 넘어가는 나무 없다 
treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        myprint("나무 넘어갑니다.")
# treeHit가 10이 되기전까지 while문 반복 수행, 10이 되면 while문 탈출

# while문 만들기 
prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
...
... Enter number: """

number = 0 # number에 0을 먼저 대입함. 이렇게 변수를 먼저 설정해 놓지 않으면 
# 다음에 나올 while 문의 조건문인 number!=4에서 변수가 존재하지 않는다는 오류 발생
while number != 4:
    myprint(prompt)
    number = int(input()) # input() : 글자로 받아오기, int() : 정수로 바꾸기
# 다른 숫자 입력하면 while 문 반복, 4 입력시 while 문 탈출


# while 문 강제로 빠져나가기 
# break 문을 이용해 강제로 while 문을 멈춤
coffee = 10
money = 300
while money:
    myprint("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    myprint(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        myprint("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# 조건문이 0 이 아니기 때문에 항상 참 (while money: 에서 money = 300) 
# while 문을 수행할 때마다 커피 개수가 하나씩 줄고 0 
# "커피가 다 떨어졌습니다. 판매를 중지합니다." 출력 후 while 문 종료 
    

# while 문의 맨 처음으로 돌아가기 
# 1 ~ 10 까지의 숫자중 홀수만 출력
# countinue 문을 이용 
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue 
    # 2로 나누었을때 나머지가 0 이면(짝수) 다시 처음으로 돌아감
    myprint(a)
# 홀수만 출력






