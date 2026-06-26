def myprint(content):
    print(content, end = "\n\n\n")
    
### 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합(intersection) 구하기
myprint(s1 & s2)
myprint(s1.intersection(s2)) # intersection 매서드 이용하기
myprint(s2.intersection(s1))

# 합집합(union) 구하기 
myprint(s1 | s2)
myprint(s1.union(s2)) # union 매서드 이용하기
myprint(s2.union(s1))

# 차잡합(difference) 구하기
myprint(s1 - s2)
myprint(s2 - s1)
myprint(s1.difference(s2)) # differencw 매서드 이용하기
myprint(s2.difference(s1))