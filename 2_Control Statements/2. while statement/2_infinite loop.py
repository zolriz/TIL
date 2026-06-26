def myprint(*data):
    print(*data, end="\n\n\n")
    
### 무한루프
# 파이썬에서는 무한루프를 while 문을 이용해 구현할 수 있음
# while Ture:
#   수행할 문장_1
#   수행할 문장_2
#   수행할 문장_3
#   ...
# while 문의 조건문이 True이므로 항상 참이 됨.
# 따라서 while 문 안에 있는 문장들은 무한히 수행됨.

while True:
    myprint("Ctrl+C를 눌러야 while 문을 빠져나갈 수 있습니다.")