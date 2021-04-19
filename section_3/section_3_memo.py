# 1. 회문 문자열 검사

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

insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]

append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
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