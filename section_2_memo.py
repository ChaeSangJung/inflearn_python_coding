# 1. K번째 약수
# 다른 방법으로...
n=6 
k=1
cnt=0
a=[]
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
        a.append(i)

if(k > len(a)):
  print(-1)
else: 
  print(a[k-1])

# 2. K번째 수
# 강의 들을 것!!

# 3. K번째 큰수
# 강의 들을 것!!

# 4. 대표값
n=10
a=[45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
ave=sum(a)/n
# 반올림 int(74.3) => 74, int(73.9) => 73
ave=ave+0.5
ave=int(ave)
min=2147000000
for idx, x in enumerate(a):
    # print(idx, ":", x)
    # 0 : 45
    # 1 : 73
    # 2 : 66
    # 3 : 87
    # 4 : 92
    # 5 : 67
    # 6 : 75
    # 7 : 79
    # 8 : 75
    # 9 : 80
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        # 조건을 x>score 로 걸었기 때문에 뒤에 같은 점수가 나와도 번호가 빠른 값이 출력이 됨
        if x>score:
            score=x
            res=idx+1
print(ave, res)

enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.

data = enumerate((1, 2, 3))
print(data, type(data))
0 : 1
1 : 2
2 : 3

for i, value in data:
    print(i, ":", value)
print()
0 : 1
1 : 2
2 : 3

dict1 = {'이름': '한사람', '나이': 33}
data = enumerate(dict1)
for i, key in data:
    print(i, ":", key, dict1[key])
print()
0 : 이름 한사람
1 : 나이 33

data = enumerate("재미있는 파이썬")
for i, value in data:
    print(i, ":", value)
print()
0 : 재
1 : 미
2 : 있
3 : 는
4 :  
5 : 파
6 : 이
7 : 썬
range([strat,] stop [,step])

# 5. 정다면체
n=4
m=6
# cnt는 횟수를 구해 넣는 list
cnt=[0]*(n+m+3)
# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 0 0 0 0 0 0 0 0 0  0  0  0 
max=0
for i in range(1, n+1):  
  for j in range(1, m+1):
    cnt[i+j]=cnt[i+j]+1

# 0 1 2 3 4 5 6 7 8 9 10 11 12
# 0 0 0 0 0 0 0 0 0 0  0  0  0
# # i=1
#     1 1 1 1 1 1
# # i=2
#       2 2 2 2 2 1
# # i=3
#         3 3 3 3 2 1
# # i=4
#           4 4 4 3 2  1
# cnt = [0 0 1 2 3 4 4 4 3 2 1 0 0]

# cnt 에서 max값 구하기
for i in range(n+m+1):
  if cnt[i]>max:
    max=cnt[i]

# max값을 기준으로 cnt에서 값과 비교하여 index 구하기
for i in range(n+m+1):
  if cnt[i]==max:
    print(i, end=' ')

# 6. 자릿수의 합
# 각 자릿수 구하는 함수
def digit_sum(x):
    sum=0
    while x>0:
        t = x%10
        sum = sum + t
        x=x//10      
    return sum

# x= 15232
# print(t, sum, x)
# 1. 2 2 1523
# 2. 3 5 152
# 3. 2 7 15
# 4. 5 12 1
# 5. 1 13 0

# 7. 소수(에라토스테네스 체)
# 1. 2부터 소수를 구하고자 하는 구간의 모든 수를 나열한다. 그림에서 회색 사각형으로 두른 수들이 여기에 해당한다.
# 2. 2는 소수이므로 오른쪽에 2를 쓴다. (빨간색)
# 3. 자기 자신을 제외한 2의 배수를 모두 지운다.
# 4. 남아있는 수 가운데 3은 소수이므로 오른쪽에 3을 쓴다. (초록색)
# 5. 자기 자신을 제외한 3의 배수를 모두 지운다.
# 6. 남아있는 수 가운데 5는 소수이므로 오른쪽에 5를 쓴다. (파란색)
# 7. 자기 자신을 제외한 5의 배수를 모두 지운다.
# 8. 남아있는 수 가운데 7은 소수이므로 오른쪽에 7을 쓴다. (노란색)
# 9. 자기 자신을 제외한 7의 배수를 모두 지운다.
# 10. 위의 과정을 반복하면 구하는 구간의 모든 소수가 남는다.
n=20
ch=[0]*(n+1)
ans=[]
cnt=0
for i in range(2, n+1):
    if ch[i]==0:
        cnt+=1
        ans.append(i)
        for j in range(i, n+1, i):
            ch[j]=1
        
print(ans, cnt)
i=2
cnt = 1
ans = [2]
for j in range(2, 20+1, 2):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 0 1 0 1 0 1 0 1  0  1  0  1  0  1  0  1  0  1

i=3
cnt = 2
ans = [2, 3]
for j in range(3, 20+1, 3):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 0 1 0 1 1 1  0  1  0  1  1  1  0  1  0  1

i=4

i=5
cnt = 3
ans = [2, 3, 5]
for j in range(5, 20+1, 5):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 0 1 1 1  0  1  0  1  1  1  0  1  0  1

i=6

i=7
cnt = 4
ans = [2, 3, 5, 7]
for j in range(5, 20+1, 5):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 1 1 1 1  0  1  0  1  1  1  0  1  0  1

i=8, i=9, i=10
i=11
cnt = 5
ans = [2, 3, 5, 7, 11]
for j in range(11, 20+1, 11):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 1 1 1 1  1  1  0  1  1  1  0  1  0  1

i=12
i=13
cnt = 6
ans = [2, 3, 5, 7, 11, 13]
for j in range(13, 20+1, 13):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 1 1 1 1  1  1  1  1  1  1  0  1  0  1

i=14, i=15, i=16
i=17
cnt = 7
ans = [2, 3, 5, 7, 11, 13, 17]
for j in range(17, 20+1, 17):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 1 1 1 1  1  1  1  1  1  1  1  1  0  1

i=18
i=19
cnt = 8
ans = [2, 3, 5, 7, 11, 13, 17, 19]
for j in range(19, 20+1, 19):
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
0 0 1 1 1 1 1 1 1 1 1  1  1  1  1  1  1  1  1  1  1

i=20


1. range(a,b) => a ~ b-1까지
2. ragne(b) => 0 ~ b-1까지
3. range(a,b,c) => a ~ b-1까지 c만큼 건너 뛰세요.
ex) range(0,50,5) => 0,5,10,...40,45,50

# 8.뒤집은 소수
# 수 뒤집기
def reverse(x):
    res=0
    while x>0:
        t=x%10
        # 나머지 값을 10단위 100단위로 순차적으로 올려준다.
        res=res*10+t
        x=x//10
    return res

# 9. 주사위 게임
# map()
# https://dojang.io/mod/page/view.php?id=2286
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
# map은 원본 리스트를 변경하지 않고 새 리스트를 생성
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
>>> a = [1.2, 2.5, 3.7, 4.6]
>>> a = list(map(int, a))
[1, 2, 3, 4]
>>> b = list(map(str, range(10)))
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# ie..
# +	더하기	a + b = 30
# -	빼기	a - b = -10
# *	곱하기	a * b = 200
# /	나누기	b / a = 2.0
# %	나머지	b % a = 0
# **	제곱	a ** c = 1000
# //	몫	a // c = 3
# [..."👩‍👩‍👦‍👦"]
# (윈도우 로고키) + (마침표키) 또는 (윈도우 로고키) + (세미콜론키)