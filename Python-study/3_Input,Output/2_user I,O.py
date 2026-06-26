def myprint(*data):
    print(*data, end="\n\n\n")
    
### 사용자 입출력 ###

# 사용자 입력 활용하기 
# 사용자가 입력한 값을 어떤 변수에 대입하고 싶을 때는 어떻게 해야할까?
# 1) input 사용하기 
a = input()
myprint(a)
# input은 사용자가 키보드로 입력한 모든 것을 문자열로 저장
# 시용자가 입력한 것을 그대로 출력 

# 2) 프롬포트를 띄워 사용자 입력 받기
# input()의 괄호 안에 안내 문구를 입력하여 프로포트를 띄워줌, input("안내_문구")
number = input("숫자를 입력하세요 : ")
myprint(number)
# input은 입력되는 모든 것을 문자열로 취급하기 때문에 number은 숫자열이 아니고 문자열이라는 것에 주의



# print 자세히 알기
# 1) 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다 
myprint("Life" "is" "too short") 
myprint("Life" + "is" + "too short")
# 위 두문장은 완전히 동일한 결괏값을 출력함, 즉 따옴표로 둘러싸인 문자열을 연속해서 쓰면 + 연산을 한 것과 같음

# 2) 문자열 띄어쓰기는 쉼표로 함 
myprint("Life", "is", "too short")
# 쉼표를 하용하면 문자열을 띄어 쓸 수 있음

# 3) 한 줄에 결괏값 출력하기 
# 한 줄에 결괏값을 게속 이어서 출력하려면 매개변수 end를 사용해 끝문자를 지정해야 함 
for i in range(10):
    print(i, end=' ')
    


