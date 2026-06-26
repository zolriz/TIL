def myprint(*data):
    print(*data, end="\n\n\n")
    
### for 문과 같이 쓰는 함수들
# for 문과 countine 문
# countine 문을 for 문에서 사용가능
# for 문을 수행하는 도중 countine 문을 만나면 for문의 처음으로 되돌아감

# for 문 응용 예제 이용
# 60점 이상인 사람에게는 축하 메세지를 보내고 나머지 사람에게는 아무런 메세지를 전하지 않음

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue # 점수가 60점 미만이면 맨 처음으로 돌아감
    myprint(f"{number}번 학생 축하합니다. 합격입니다.")


# for 문과 range 함수
# for 문은 숫자 리스트를 자동으로 만들어 주는 range 함수와 함께 사용하는 경우가 많음

# range 함수 사용법
a = range(10) 
myprint(a) 
# range(0, 10)은 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어 줌
# range(0, 10) - 0,1,2,3,4,5,6,7,8,9
a = range(1, 11) 
myprint(a) 
# 시작 숫자와 끝 숫자를 자정하려면 range(시작_숫자, 끝_숫자) 형태를 사용하는데,
# 이때 끝 숫자는 포함되지 않음
# range(1, 11) - 1,2,3,4,5,6,7,8,9,10

# for 과 range 함수 예시
# 1부터 10까지 더하기
add = 0
for i in range(1, 11):
    add = add + i

print(add)
# i 에 숫자가 1부터 10까지 하나씩 대입되면서 
# add = add + i 문장을 반복적으로 수행하고 add는 최종적으로 55가됨


# 합격축하 에시 range 함수로 표현하기 
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    myprint(f"{number + 1}번학생 축하합니다. 합격입니다.")
# len는 리스트 안의 요소 개수를 리턴하는 함수.
# 따라서 range(len(marks))는 range(5)가 됨 number에는 0,1,2,3,4 대입됨
# marks 리스트를 순서대로 인덱싱한 후, 60점 미만이면 처음으로 돌아가고, 60점 이상인 경우만 출력


# 1부터 100 까지 더하기 (for 과 range 이용)
for a in range(111):
    b = 0
    c = a + b

myprint(c)


# for 과 range 를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ") # 곱셈 계산 후 한칸 띄움
    print(' ') # print(' ') - 자동 줄 바꿈
# 처음에 i에 2넣고 번복문 시작, j에 1부터 9까지 넣을때 까지 반복 
# 그리고 줄 바꾸고 i 반복 


    


