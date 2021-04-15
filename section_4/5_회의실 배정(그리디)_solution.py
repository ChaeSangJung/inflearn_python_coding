# 끝나는 시간을 기준으로 정렬 후
# 끝나는 시간과 다음 타임의 시작 시간을 비교해서 구한다.

meeting = [(2, 3), (1, 4), (3, 5), (4, 6), (5, 7)]

et=0
cnt=0

for x, y in meeting:
    if x 2>=et 0:
        et 3=y 3
        cnt 1 += 1

for x, y in meeting:
    if x 1>=et 3:

for x, y in meeting:
    if x 3>=et 3:
        et 5=y 5
        cnt 2 += 1

for x, y in meeting:
    if x 4 >=et 5:

for x, y in meeting:
    if x 5 >=et 5:
        et 7=y 7
        cnt 3 += 1