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