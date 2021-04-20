# 5. 수들의 합
# 강의 들을 것!

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