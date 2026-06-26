def myprint(content):
    print(content, end="\n\n")

### 딕셔너리 관련 함수

# 1. keys - key리스트 만들기 
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
myprint(a.keys())
# 참고) 파이썬 3.0 이후에서는 a.keys()함수를 호출하면 dict_keys[]를 리턴함
# 리스트만 리턴하고 싶으면 list(a.keys())를 사용해야함 
myprint(list(a.keys()))

for k in a.keys(): # a에있는 key들을 하나씩 꺼내어 k에 할당, 계속 반복
    myprint(k) # k 출력

# 2. values - value리스트 만들기
myprint(a.values()) 
myprint(list(a.values()))

# 3. items - key와 value 쌍으로 얻기 
myprint(a.items())

# 4. clear - key, value 쌍 지우기
myprint(a.clear())

# 5. get - key로 value 얻기
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
myprint(a.get('name'))
myprint(a.get('nokey')) 
# print(a[])와 print(a.get[])의 차이 - a는 키가 없으면 애러가 뜨고 get은 키가 없으면 none이 뜸

# 6. in - 해당 key가 딕셔너리 안에 있는지 조사하기
myprint('name' in a) # 있으면 ture
myprint('email' in a) # 없으면 false 뜸





