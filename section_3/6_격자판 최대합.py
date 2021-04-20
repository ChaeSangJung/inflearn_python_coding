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