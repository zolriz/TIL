def myprint(content):
    print(content, end="\n\n")

### f 문자열 포매팅 - {} 사이는 하나의 파이썬 코드가 실행되는 터미널로 생각
# f 문자열 포매팅 : 문자열 앞에 f를 붙이면 f문자열 포메팅 사용가능

name = '홍길동'
age = 30 
myprint(f"나의 이름은 {name}입니다. 나이는 {age}입니다")

material = 'steel'
f_y = 400
myprint(f"부재 이름 : {material} 항복점 : {f_y}Mpa")

# f 문자열은 표현식 지원 (표현식 : 중괄호 안의 변수를 계산식과 함께 사용)
age = 30
myprint(f"내년이면 {age + 1}살이 된다")

# f 문자열에서 딕셔너리 사용 (딕셔너리 : 데이터를 key 와 value 의 쌍으로 저장하는 자료형)
d = {'name' : '홍길동', 'age' :30}
myprint(f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.")



# f 문자열에서 정렬 
### f-string : 뒤에 순서 [채울문자][정렬][부호][#][0][너비][쉼표][.정밀도][타입]
myprint(f"{"hi":<10}")
myprint(f"{"hi":>10}")
myprint(f"{"hi":^10}")


# f 문자열에서 공백 체우기
myprint(f"{"hi":=^10}")
myprint(f"{"hi":!<10}")

### f-string 숫자 포맷팅 순서 [부호][너비][구분자][.소수점][타입]
number = 1234.5678
myprint(f"{number:+15,.2f}")


# f-string 소수점 표현하기 
y = 30.42134234
myprint(f"{y:10.4f}")

# f-string {} 표현하기
myprint(f"{{and}}")