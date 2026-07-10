def myprint(content):
    print(content, end="\n\n")

### 문자열 자료형 ###
# 문자열 : 문자, 단어 등으로 구성된 문자들의 집합, '123' 이여도 ''안에 있어서 문자열이라 볼 수 있음



# 문자열 만들기 "  ", '  ', """  """, '''  '''
myprint("Hellow World")
myprint('Python is fun')
# 파이썬에서 따옴표 2개는 "" "", '' '' 는 빈거 라고 생각함 따라서 사용x
myprint("""Life is too short, You need python""")
myprint('''Life is too short, You need python''')



# 문자열에 작은따옴표 표현 - 작은따움표 쓰고 큰따옴표로 닫기 
myprint("Python's favorite food is perl")

# 문자열에 큰따옴표 표현 - 큰따옴표 쓰고 작은따옴표로 닫기
myprint('"Python is very easy."he says.')
# 참고) myprint(""Python is very easy." he says.") ""문자열 인식, Python is very easy - 오류, "he says." 문자열 인식

# 역슬래시(\)를 사용해 작은따옴표와 큰따옴표 문자열에 포함하기 - \뒤의 작음 따옴표와 큰따옴표는 그 자체를 의미
myprint("Python\'s favorite food is perl")
myprint("\"Python is very easy.\" he says.")


# 여러줄 문자열 표현 
# 이스케이프 코드 \n 삽입 
myprint("Life is too short\nYou need python")

# 따옴표(큰거 or 작은거) 3개 사용하기 
myprint(''' 
Life is too short
You need python
        ''')
myprint("""
Life is too short
You need python
        """)


## 이스케이프 코드 ##
# 이스케이프 코드 - 일반적인 문자로 표현하기 어려운 특수한 동작이나 특수 문자를 나타내기 위해 사용하는 약속된 기호
# \n 줄 바꿈
# \t 탭 간격 띄우기
# \\ \를 표현
# \' '를 표현
# \" "를 표현


# 문자열 연산하기 - 문자열을 더하거나 곱할 수 있음
# 문자열 더하기
head = "Python"
tail = " is fun"
myprint(head + tail)

# 문자열 곱하기
a = "python"
myprint(a * 2)

print("=" * 50)
print(f"{"My Program":^50}")
myprint("=" * 50)


# 문자열 길이 구하기 - len(lenth)
a = "Life is too short"
myprint(len(a))


 





