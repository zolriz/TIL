def myprint(content):
    print(content, end="\n\n")

### 딕셔너리 자료형 (dictionary는 영어로 '사전' 이라는 의미)
# 딕셔너리는 key와 value를 한쌍으로 가지는 자료형, 
# 리스트나 튜플 처럼 순차적으로 해당 요솟값을 구하지 않고 key를 통해 value를 얻음

# 딕셔너리 형태
# key와 value의 쌍 여러개가 {}로 둘러싸여 있고, 각각의 요소는 key:value 형태로 이루어져 있고 쉼표(,)로 구분됨
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

a = {1: 'hi'} # key로 정수값, value로 문자열 'hi'
a = {'a': [1, 2, 3]} # value에 리스트 넣기 가능 




### 딕셔너리 쌍 추가, 삭제
# 딕셔너리 쌍 추가하기 
a = {1: 'a'}
a[2] = 'b' # 2라는 key가 있으면 기준값을 'b'로 바꾸고 없으면 새로 만듬
myprint(a)
a['name'] = 'pey' # 'name': 'pey' 추가
myprint(a)

# 딕셔너리 요소 삭제하기
del a[1] # 1인 key와 value삭제
myprint(a)



# 딕셔너리 사용하는 방법
# 딕셔너리 key를 사용해 value 얻기 
grade = {'pey': 10, 'julliet': 99}
myprint(grade['pey'])
myprint(grade['julliet'])

a = {1: 'a', 2: 'b'}
myprint(a[1])
myprint(a[2])

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
myprint(dic['name'])
myprint(dic['phone'])
myprint(dic['birth']) 
# key 값을 출력하면 value 값을 리턴함




### 딕셔너리 만들때 주의할 사항
# 중복되는 key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨 - key는 고유한 값이기 때문
a = {1: 'a', 1: 'b'}
myprint(a)

# key에는 리스트 사용 할 수 없지만, 튜플은 사용가능함 단, value에는 아무값이나 넣을 수 있음
'''
a = {[1,2] : 'hi'} - 에러 뜸
'''



