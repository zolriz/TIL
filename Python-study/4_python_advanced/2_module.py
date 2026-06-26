def myprint(*data):
    print(*data, end="\n\n\n")
    
### 모듈 ###
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일임


## 모듈 불러오기 
import mod1
myprint(mod1.add(3, 4))
myprint(mod1.sub(4, 2))
# import함수는 이미 만들어 놓은ms 파이썬 모듈을 사용할 수있게하는 명령어
# mod1.py에 있는 add 함수를 사용하기 위해선 mod.add 처럼 모듈 이름 뒤 도트 연산자를 붙임
# import 사용 방법 : import 모듈_이름

# add, sub 처럼 함수 이름 만 쓰고 싶은경우
# from 모듈_이름 import 모듈_함수 처럼 사용
from mod1 import add
myprint(add(3,4))
# add 함수와 sub 함수 둘다 사용하기
from mod1 import add, sub
myprint(sub(3,4))
# from 모듈_이름 import 모듈_함수1, 모듈_함수2



