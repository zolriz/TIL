def myprint(content):
    print(content, end="\n\n")

### 리스트의 슬라이싱과 인덱싱
# 리스트 인덱싱
a = [1, 2, 3]
myprint(a)
myprint(a[0]) # a[0]은 리스트의 첫번쨰 요소값
myprint(a[0] + a[2]) 
myprint(a[-1]) # a[-1]은 리스트이 마지막 요소값
# 이중 리스트 인덱싱
a = [1, 2, 3, ['a', 'b', 'c']]
myprint(a[0])
myprint(a[-1]) # ['a', 'b', 'c'] 출력
myprint(a[3]) # ['a', 'b', 'c'] 출력
myprint(a[-1][0]) # ['a', 'b', 'c']안의 'a' 출력 
myprint(a[-1][1]) # ['a', 'b', 'c']안의 'b' 출력
myprint(a[-1][2]) # ['a', 'b', 'c']안의 'c' 출력
# 삼중 리스트 인덱싱
a = [1, 2, ['a', 'b', ['Life', 'is']]]
myprint(a[2][2][0] + ' ' + a[2][2][1])


# 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
myprint(a[0:2]) # 문자열 슬라이싱이랑 비슷
b = a[:2] # 처음부터 a[1] 까지
c = a[2:] # a[2] 부터 마지막 까지
myprint(b)
myprint(c)
# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
myprint(a[2:5]) # a[2] 부터 a[4] 까지
myprint(a[3][:2])