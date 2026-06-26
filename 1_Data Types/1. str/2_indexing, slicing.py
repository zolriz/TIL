def myprint(content):
    print(content, end="\n\n")



### 문자열 인덱싱 - 문자열을 가르킴, 0부터 시작
a = "Life is too short, You need Python"
# L=0, i=1, f=2, e=3, ' '=4, i=5...
myprint(a[3])

# 인덱싱 활용
myprint(a[0]) # 0번째
myprint(a[12]) # 12번째
myprint(a[-1]) # 뒤에서 첫번째
myprint(a[-0]) # a[0]과 같음 
myprint(a[-2]) # 뒤에서 두 번째
myprint(a[-5]) # 뒤에서 다섯 번째 




###문자열 슬라이싱 - 문자열을 자름
# a[시작_번호:끝_번호] = 시작_번호 <= a < 끝_번호
a = "Life is too short, You need Python"
myprint(a[0:4]) # 'Life'
myprint(a[0:3]) # 'Lif'
myprint(a[0:5]) # 공백 포함해서 표현
myprint(a[5:7]) # 'is '
myprint(a[12:17]) # 'short'

# a[시작_번호:] - 시작_번호부터 끝까지
myprint(a[19:])
# a[:끝_번호] - 처음_번호부터 끝까지
myprint(a[:17])
# a[:] - 처음부터 끝까지
myprint(a[:])
# a[19:-7] - 19번째부터 뒤에서 7번째까지



## 슬라이싱 활용 
# 날씨 날짜 표현
a = "20230331Rainy"
year = a[:4]
month = a[4:8]
weather = a[8:]
myprint(year)
myprint(month)
myprint(weather)


# 문자열 고치기
b = "Pithon"
myprint(b[:1] + 'y' + b[2:])



