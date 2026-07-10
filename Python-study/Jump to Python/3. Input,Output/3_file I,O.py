def myprint(*data, end="\n\n\n"):
    print(*data)
    
### 파일 읽고 쓰기 ###

# 파일 생성하기
f = open("새파일.txt", 'w')
f.close()
# 파일을 생성하기 위해 파이썬 내장 함수 open을 사용
# open 함수는 '파일 이름'과 '파일 열기 모드'를 입력값으로 받고 결괏값으로 파일 객체를 리턴함
# 파일_객체 = open(파일_이름, 파일_열기_모드)

# 파일 열기 모드 
# r - 읽기 모드 : 파일을 읽기만 할 떄 사용함
# w - 쓰기 모드 : 파일에 내용을 쓸 떄 사용함
# a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용함 
# 파일을 쓰기 모드로 열면 해당파일이 이미 존재할 경우 원래 있던 내용이 모두 사라지고 해당 파일이 존재하지 않으면 새로운 파일이 생성됨 
f = open("새파일.txt", 'w')
f.close()
# f.close()는 열려 있는 파일 객체를 닫아 주는 역활을 함, 사실 생략해도 무방함 프로그램을 종료할 때 파이썬 프로그램이 열려있는 파일의 객체를 자동으로 닫아주기 때문
# 하지만 close()를 사용해 닫이 주는게 좋음, 쓰기모드로 열었던 파일을 닫지 않고 그대로 사용하면 오류가 발생 하기 때문 



# 파일을 쓰기모드로 열어 내용 쓰기
f = open("새파일.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i 
    f.write(data) # data를 파일 객체 f에 써라
f.close()



# 파일을 읽는 여러가지 방법 

# 1) readline 함수 이용하기 
f = open("새파일.txt", 'r', encoding='utf-8')
line = f.readline()
myprint(line)
f.close()
# '새파일.txt'파일을 읽기 모드로 연 후 readline()을 사용해서 첫 번째 줄을 읽어 출력하는 에제

# 2) readlines 함수 사용하기
# 모든 줄을 출력하고 싶다면
f = open("새파일.txt", 'r', encoding='utf-8')
while True:
    line = f.readlines()
    if not line: break
    print(line)
f.close()
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴함

# 3) read 함수 사용하기 
f = open("새파일.txt", 'r', encoding='utf-8')
data = f.read()
myprint(data)
f.close()
# f.read()는 파일의 내용 전체를 문자열로 리턴함

# 4) 파일 객체를 for 문과 함께 사용하기 
f = open("새파일.txt", 'r', encoding='utf-8')
for line in f:
    myprint(line)
f.close()
# 파일 객체는 기본적으로 위와 같이 for문과 함께 사용하여 파일을 줄 단위로 읽을 수 있음 

# 5) 파일에 새로운 내용 추가하기 
# 원래 있던 값을 유지하면서 새로운 값만 추가하는 경우
# 추가 모드('a')로 열기 
f = open("새파일.txt", 'a', encoding='utf-8')
for i in range(11, 21):
    data = "%d번째 줄입니다\n" % i 
    f.write(data)
f.close()
# 새파일.txt 파일을 열어 보면 원래 있던 내용 뒤에 새로운 내용이 추가된 것을 확인항 수 있음

# 6) with문과 함께 사용하기 
# with문은 자동으로 파일을 열고 닫아 주는 역활
with open("foo.txt", 'w', encoding='utf-8') as f:
    f.write("Life is too short, you need python")
    
    

