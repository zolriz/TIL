def myprint(*data):
    print(*data, end="\n\n")

### 되새김 문제 

# 1. 조건문의 참과 거짓
# 다음 코드의 결괏값은 무엇일까?
a = "Life is too short, you need python"
if "wife" in a: myprint("wife")
elif "python" in a and "you" not in a: myprint("python")
elif "shirt" not in a: myprint("need")
else: myprint("none")



# 2. 3의 배수의 합 구하기 
# while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구하기 
result = 0 
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나눠서 나머지가 0일 떄, 즉 3의 배수 
        result += i
    i += 1 # i를 1씩 증가시킴
    
myprint(result)



# 3. 별 표시하기
# while 문을 사용해 별(*)을 표시하는 프로그램 작성하기
i = 0 
while True:
    i += 1
    if i > 5 :break
    myprint('*'*i)
    
    
    
# 4. 1부터 100까지 출력하기
# for 문을 사용해 1부터 100까지의 숫자 출력하기
for i in range(1, 101):
    myprint(i)



# 5. 평균 점수 구하기 
# for 문을 사용하여 학생들의 평균 점수 구하기
# [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0 
for score in A: 
    total += score
average = total/10
myprint(average)



# 6. 리스트 컴프리헨션 사용하기 
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
myprint(result)
# 리스트 컴프리헨션 사용
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 ==1]
myprint(result)


