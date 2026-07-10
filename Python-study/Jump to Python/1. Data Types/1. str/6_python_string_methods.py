def myprint(content):
    print(content, end="\n\n\n")

## 문자열 내장 함수 : 문자열 자료형은 자체적으로 함수를 가지고 있음. 문자열 변수 이름 뒤에 '.'를 붙인 후 함수 이름을 쓰면 됨
# 문자 개수 세기 count
a = "hobby"
myprint(a.count("b"))



# 위치 알려 주기1 - find : 문자열이 처음 나온 위치를 알려줌, 찾는 문자열이 존재 하지 않으면 -1을 반환
a = "Python is the best choice"
myprint(a.find("b"))    
myprint(a.find('e'))

# 위치 알려 주기2 - index : 문자열이 처음 나온 위치를 알려줌, 찾는 문자열이 존재 하지 않으면 오류 발생
a = "life is too short"
myprint(a.index('t'))
myprint(a.index('s'))



# 문자열 삽입 join - 리스트나 튜플도 사용가능
myprint('""'.join('abcd'))
myprint(",".join(['a', 'b', 'c', 'd']))




# 소문자를 대문자로 바꾸기 upper
myprint("hi".upper())

# 대문자를 소문자로 바꾸기 lower 
myprint("HI".lower())



# 공백 채우기 - strip
# 왼쪽 - lstrip
a = "      hi      "
myprint(a.lstrip())
# 오른쪽 - rstrip
myprint(a.rstrip())
# 양쪽 - strip
myprint(a.strip())



# 문자열 바꾸기 - replace : replace(바뀔 문자열, 바꿀 문자열)
a = "Life is too short"
myprint(a.replace("Life", "Your leg"))



# 문자열 나누기 - split /나눈 값은 리스트에 하나씩 들어감
# split() - 공백을 기준으로 문자열 나눔 
myprint(a.split())

# split(":") - :을 기준으로 문자열 나눔
b = "a:b:c:d"
myprint(b.split(':'))