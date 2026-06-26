def myprint(*data):
    print(*data, end="\n\n\n")
    
    
### for 문
# while 문과 비슷한 반복문인 for 문은 문장 구조가 한눈에 들어 온다는 장점이 있음
# for 문의 기본구조
# for 변수 in 리스트(또는 튜플, 문자열):
#   수행할_문장1
#   수행할_문장2
#   수행할_문장3
#   ...

# 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어
# '수행할_문장1','수행할_문장2' 등이 수행됨


# 1. 전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    myprint(i)
# 'one'이 먼저 i 변수에 대입된 후 print(i) 문장을 수행함. 
# 다음에 두 번쨰 요소 'two'가 i 변수에 대입된 후 print(i) 
# 문장을 수행하고 리스트 마지막 요소 까지 이것을 반복함.


# 2. 다양한 for 문의 사용
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    myprint(first + last)
    
    
# for 문의 응용
# "총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면
# 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오."

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        myprint(f"{number}번 학생은 합격입니다.")
    else:
        myprint(f"{number}번 학생은 불합격입니다.")
# marks에 있는 요소들을 순서대로 하나씩 꺼내어 mark에 대입
# number에 숫자를 하나 더하고, 점수에 따라 합격 or 불합격 출력






 