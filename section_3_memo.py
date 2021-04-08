# 1. 회문 문자열 검사

# 2. 숫자만 추출
s="g0en2Ts8eSoft0"
res=0
for x in s:  
  if x.isdecimal():
    res=res*10+int(x)
  print(res)

# 1. res = 0*10 + 2 (2)
# 2. res = 2*10 + 8 (28)
# 3. trd = 28*10 + 0 (280)

cnt=0
for i in range(1, res+1):
  # res를 res길이만큼 구해서 1~res길이의 수로 나누어서 나머지(%)가 0인 숫자가 약수
  if res%i==0:
    cnt+=1
print(cnt)

# 3. 카드역배치
# 강의 들을 것!

# 4. 두 리스트 합치기
n=3
a=[1, 10, 3]
m=5
b=[2, 3, 6, 7, 9]

a.sort()
b.sort()

p1=p2=0
c=[]

while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
# a에서 10이라는 숫자때문에 p1 = 2에서 멈췄고(p2는 5까지 다 돌고 while문을 빠져 나왔다.)
# a의 10만 남아 있으니 c[]에 합쳐 줘야 한다. 제일 큰 수이니 뒤에 붙이면 된다.
# [3:] index = 3부터 끝까지
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')

# 5. 수들의 합
# 강의 들을 것!

# 6. 격자판 최대합
n=5
a=[
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19]
]

largest = 0
for i in range(n):  
  sum_verti = sum_hori=0 # 행 또는 열 한번 돌고 초기화
  for j in range(n):
    # 행들의 합 (a[0][0]+a[0][1]+a[0][2]+a[0][3]+a[0][4], a[1][1]+a[1][1]+a[1][2]+a[1][3]+a[1][4], ..., a[4][0]+a[4][1]+a[4][2]+a[4][3]+a[4][4])
    sum_verti += a[i][j]
    # 열들의 합 (a[0][0]+a[1][0]+a[2][0]+a[3][0]+a[4][0], a[0][1]+a[1][1]+a[2][1]+a[3][1]+a[4][1], ..., +a[0][4]+a[1][4]+a[2][4]+a[3][4]+a[4][4])
    sum_hori += a[j][i]
  if sum_verti > sum_hori and sum_verti > largest:
    largest = sum_verti
  if sum_verti < sum_hori and sum_hori > largest:
    largest = sum_hori    

sum_dia_forward = sum_dia_reverse = 0
for i in range(n):
  # 대각선 좌상에서 우하로
  sum_dia_forward += a[i][i]
  #  대각선 우상에서 좌하로
  sum_dia_reverse += a[i][n-i-1]
if sum_dia_forward > sum_dia_reverse and sum_dia_forward > largest:
  largest = sum_dia_forward
if sum_dia_forward < sum_dia_reverse and sum_dia_reverse > largest:
  largest = sum_dia_reverse

print(largest)

# 7. 사과나무
n=5
a= [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19]
]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

s=2, e=2
i=0
range(2, 2+1)
  res = a[0][2]
  i=0 < n//2 => s=1, e=3

i=1
range(1, 3+1)
  res = a[1][1] + a[1][2] + a[1][3]
  i=0 < n//2 => s=0, e=4

i=2
range(0, 4+1)
  res = a[2][0] + a[2][1] + a[2][2] + a[2][3] + a[2][4]
  else s = 1, e = 3
i=3
range(1, 3+1)
  res = a[3][1] + a[3][2] + a[3][3]
  else s = 2, e = 2
i=4
range(2, 2+1)
  res = a[4][2]
  else s = 3, e = 1

# 8. 곳감
# 강의 들을 것!

# 9. 봉우리
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=5
a=[
  [5, 3, 7, 2, 3],
  [3, 7, 1, 6, 1],
  [7, 2, 5, 3, 4],
  [4, 3, 6, 4, 1],
  [8, 7, 3, 5, 2]
]

a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
  x.insert(0, 0)
  x.append(0)

# 이 이하부터 이해가 안됨
# cnt=0
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
#             cnt+=1
# print(cnt)

# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]

# append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]

# 10. 스도쿠 검사
# 강의 들을 것!

# 11. 격자판 회문수
for i in range(3):
  for j in range(7):
    tmp=board[j][i:i+len]
    
    if tmp==tmp[::-1]:
      cnt+=1
    # 여기 까지 이해가 됨, 하나 부족하게 나옴
    # 이 이하는 무엇을 위한 코드인지 모르겠음
    for k in range(len//2):
      if board[i+k][j]!=board[len-k+i-1][j]:
        break;
    else:
      cnt+=1
        
print(cnt)