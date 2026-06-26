
"""
포멧코드와 숫자 사용
"""
def myprint(content):
    print(content, end="\n\n") 

# 오른쪽 정렬 (10개의 길이 중 앞에 8개 공백)
myprint("%10s" % "hi")

# 왼쪽 정렬 (10개의 길이 중 뒤에 8개 공백) + jane 
myprint("%-10sjane" % "hi")


# 소수점 표현하기 
# 길이x 소수점 뒤 4자리
myprint("%0.4f" % 3.42134234)

# 전체길이 10개 소수점 뒤 4자리
myprint("%10.4f" % 3.42134234)



#format 함수를 사용한 포매팅 - (인덱스는 0,1,2,.. 순서로 포메팅)
#인덱스는 데이터가 저장된 위치(주소)를 가리키는 고유한 이름표이다

myprint("I eat {0} apples" .format(3))
myprint("I eat {0} apples" .format("five"))

number = 3
myprint("I eat {0} apples" .format(number))

number = 10
day = "three"
myprint("I ate {0} apples. so I was sick for {1} days" .format(number, day))

# {}사이에 name 넣기, format함수에는 반드시 name = value 를 지정해야함
myprint("I ate {number} apples. so I was sick for {day} days." .format(number=10, day=3))

# 인덱스와 이름을 혼용해서 넣기
myprint("I ate {0} apples. so I was sick for {day} days" .format(10, day=3))


#윈쪽 정렬 :<
myprint("{0:<10}" .format("hi"))

#오른쪽 정렬 :>
myprint("{0:>10}" .format("hi"))

#가운데 정렬 :^
myprint("{0:^10}" .format("hi"))

#정렬 공백 채우기 - 채울 문자는 < > ^ 앞에 붙여야함
myprint("{0:=^10}" .format("hi"))
myprint("{0:!<10}" .format("hi"))

#소수점 표현하기 -0.xf x자리마늠 소수점 표현
x = 3.421123124
myprint("{0:0.4f}" .format(x))

#{} 문자 자체를 표현 - {{}} 중괄호 2번쓰기 ({} 일때는 데이터 구멍으로 인식함 따라서 format()에 지정 필요)
myprint("{{}}" .format())

