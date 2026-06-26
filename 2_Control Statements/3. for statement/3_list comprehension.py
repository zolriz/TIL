def myprint(*data):
    print(*data, end="\n\n\n")

### 리스트 컴프리헨션
# 리스트 안에 for문을 포함하는 리스트 컴프리헨션을 사용하면 좀 더 편리하고
# 직관적인 프로그램을 만들 수 있음

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
# append 함수는 리스트의 가장 끝에 새로운 요소를 추가할 때 사용
myprint(result)
# a 리스트의 각 항목에 3을 곱한 결과를 result 리스트에 담음

# 리스트 컴프리헨션 사용시 
# append 함수를 사용하는 대신 바로 리스트 안으로 집어 넣음
a = [1, 2, 3, 4]
result = [num*3 for num in a]
myprint(result)

# [1, 2, 3, 4] 중에서 짝수에만 3을 곱하여 담고 싶다면 리스트 컴프리헨션 안에 if 조건문 사용
a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2 == 0]
myprint(result)


# 리스트 컴프리헨션 표현법 
# [표현식 for 항목 in 반복_가능_객체 if 조건문]

# 식 2개 이상 사용시 
# [표현식 for 항목1 in 반복_가능_객체 if 조건문
#  표현식 for 항목2 in 반복_가능_객체 if 조건문
#  ...
#  표현식 for 항목ㅜ in 반복_가능_객체 if 조건문]


# 리스트 컴프리헨션을 사용해 구구단의 결과를 리스트 안에 담기 
result = [x*y for x in range(2, 10) 
              for y in range(1, 10)]
myprint(result)
# x가 시침 y가 분침이라고 생각 


