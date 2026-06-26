def myprint(*data):
    print(*data)
    
### 프로그램의 입출력 ###
# 대부분의 명령 프롬포트에서 사용하는 명령어는 다음과 같이 인수를 전달하여 프로그램을 실행하는 방식을 따름 
# 명령어 [인수1 인수2 ...]
# 이러한 기능을 파이썬 프로그램에도 적용할 수 있음 


# sys 모듈 사용하기 
# 파이썬에서는 sys 모듈을 사용하여 프로그램에 인수를 전달할 수 있음 
# sys 모듈을 사용하려면 import 명령어를 사용해야 함 

import sys
args = sys.argv[1:]
for i in args:
    print(i)
# 위는 프로그램 실행 시 전달받은 인수를 for 문을 사용해 차레대로 하나씩 출력함
# sys 모듈의 argv는 프로그램 실행 시 전달된 인수를 의미함 
# 파일이름.py aaa bbb ccc 와 같이 입력했다면 argv[0]은 파일 이름이 되고 argv[1] 부터는 뒤에 따라오는 인수가 차례대로 argv의 요소가 됨 

args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')