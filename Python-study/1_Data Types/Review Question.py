def myprint(*data):
    print(*data, end="\n\n\n")
    
### 되새김 문제

# 1. 평균 점수 구하기 
국어 = 80
영어 = 75
수학 = 55
myprint((국어 + 영어 + 수학)/3)


# 2. 홀수 짝수 판별하기 
myprint(13/2)


# 3. 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
myprint(f"yyyymmdd : {yyyymmdd}")
myprint(f"num : {num}")


# 4. 주민등록번호 인덱싱
pin = "881120-1068234"
myprint(pin[-7])


# 5. 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":", "#")
myprint(b)


# 6. 리스트 역순 정렬하기 
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
myprint(a)


# 7. 리스트를 문자열로 만들기 
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
myprint(result)


# 8. 튜플 더하기 
a = (1, 2, 3)
b = a + (4,) # 튜플의 숫자가 하나일땐 콤마를 붙여야 튜플로 인식함  
myprint(b)


# 9. 딕셔너리의 키 
a = dict()
# 다음 중 오류가 발생하는 경우는?
# 딕셔너리의 키로 사용할 수 있는 자료형과 없는 자료형 구분하기 
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python' - 사용 불가
a[250] = 'python'
myprint(a)
# 딕셔너리 키의 특징
# 1. 불변 : 값이 변하지 않는 자료형은 키로 쓸 수 있음 (문자열, 숫자, 튜플)
# 2. 가변 : 값이 변할 수 있는 자료형은 키로 쓸 수 없음 (리스트, 딕셔너리)


# 10. 딕셔너리 값 추출하기 
a = {'A':90, 'B':80, 'C':70}
result = a.pop('B') 
myprint(a)
myprint(result)
# pop 매커니즘 
# 1. 제거 : 딕셔너리에 있는 'B':80 제거
# 2. 반환 : 튀어나온 값(80)이 result 라는 변수에 들어감


# 11. 리스트에서 중복 제거하기 
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aset = set(a)
myprint(aset) # set을 사용하면 중복을 제거해줌
b = list(aset)
myprint(b) # set을 다시 리스트로 변환

# 12. 파이썬 변수 
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 
# b 값은 어떻게 될까? 그리고 이런 결과가 나타나는 이유를 설염해 보자.
a = b = [1, 2, 3]
a[1] = 4
myprint(b)
# b도 [1, 4, 3]으로 출력 될 것 같다. a=b로 지정해
# 동일한 객체를 사용하고 있기 때문이다. 
# 추가) 동일한 메모리 주소를 사용하고 있기 때문




