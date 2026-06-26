def myprint(content):
    print(content, end="\n\n")

### 참고) 함수 vs 매서드
# 함수 : 독립적으로 존재하는 기능. 특정 데이터에 속해있지 않고, 이름을 불러 실행 
# 함수이름(인자)
# 매서드 : 특정 객체 안에 포함된 함수 파이썬에서는 문자열, 리스트, 딕셔너리 등이 자신만의 전용 함수를 가지고 있음.
# 객체.메서드이름(인자)

### 참고) 객체(object)란?
# 데이터(속성)와 그 데이터를 처리하는 기능(메서드)을 하나로 묶어놓은 실체 


### 리스트 관련 함수

# 1. append - 리스트에 요소 추가하기 - .append(x)는 리스트 맨 마지막에 x 추가함
a = [1, 2, 3]
a.append(4)
myprint(a)
# 리스트안에는 어떤 자료형도 추가할 수 있음
a.append([5, 6])
myprint(a)

# 2. sort - 리스트 정렬 - 리스트의 요소를 순서대로 정렬해 줌
a = [1, 4, 3, 2]
a.sort() 
myprint(a)
a = ['b', 'a', 'c'] # 알파벳도 순서대로 정렬
a.sort()
myprint(a)

# 3. reverse - 리스트 뒤집기 - 현재 리스트 요소들을 그대로 거꾸로 뒤집어줌
a = ['a', 'c', 'b']
a.reverse()
myprint(a)

# 4. index - 인덱스 반환 - index(x) 함수는 리스트에 x 값이 있으면 x의 인덱스 값(위치값)을 리턴함
a = [1, 2, 3]
myprint(a.index(3))
myprint(a.index(1))

# 5. insert - 리스트의 요소 삽입 - insert(a, b)는 리스트의 a번째 위치에 b를 삽입함
a = [1, 2, 3]
a.insert(0, 4)
myprint(a)
a.insert(3, 5)
myprint(a)

# 6. remove - 리스트 요소 제거 - remove(x)는 첫 번째로 나오는 x를 제거함 
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
myprint(a)
a.remove(3)
myprint(a)

# 7. pop - 리스트 요소 끄집어 내기 - pop(x)는 리스트의 x번쨰 요소를 리턴하고 그 요소는 삭제한다
a = [1, 2, 3]
myprint(a.pop(1)) 
myprint(a)

# 8. count - 리스트에 포함된 요소 x의 개수 세기 - count(x)는 라스트 안에 x가 몇 개 있는지 조사하여 그 개수를 리턴하는 함수임 
a = [1, 2, 3, 1]
myprint(a.count(1))

# 9. extend - 리스트 확장 - extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더하게 됨
a = [1, 2, 3]
a.extend([4, 5])
myprint(a)
b = [6, 7]
a.extend(b)
myprint(a)
 