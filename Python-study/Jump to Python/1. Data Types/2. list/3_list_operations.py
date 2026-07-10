def myprint(content):
    print(content, end="\n\n")


### 리스트 연산하기
# 리스트 더하기 (+)
a = [1, 2, 3]
b = [4, 5, 6]
myprint(a + b)

# 리스트 반복하기 (*)
a = [1, 2, 3]
myprint(a * 3)

# 리스트 길이 구하기 - len 사용
a = [1, 2, 3]
myprint(len(a))

'''
리스트 연산 오류
a = [1, 2, 3]
myprint(a[2] + "hi")
리스트는 숫자 인데 숫자 + 문자열은 더할 수 없기 때문
리스트를 문자열로 바꿔 해결
'''
a = [1, 2, 3]
myprint(str(a[2]) + "hi")




### 리스트의 수정과 삭제 
# 리스트의 값 수정하기
a = [1, 2, 3]
a[2] = 4 # 리스트의 3을 4로 바꿈
myprint(a)

# del 함수를 이용해 리스트 요소 삭제 
# del 은 리스트 내장 함수임 - del a[x] 는 x번째 요소를 삭제함
a = [1, 2, 3, 4, 5]
del a[2:]
myprint(a)



