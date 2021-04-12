# 1. 이분검색
n=8 
m=81
a=[23, 87, 65, 12, 57, 32, 99, 81]
a.sort() # a=[12, 23, 32, 57, 65, 81, 87, 99]
print(a)
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2    
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

rt(7) = 8-1
while 0 <= 8-1(7)
    mid:3 = 0+7//2
    elif a[3]:12 < 81
        lt:4 = 3 + 1 

while 4 <= 7
    mid:5 = 4+7//2
    if a[5]:81 = 81
        print(5 + 1)

answer is 6

# 2. 랜선자르기
# 강의 들을 것
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    print(cnt)
    return cnt

k=4
n=20
Line=[802, 743, 457, 539]
res=0
largest=max(Line)

# for i in range(k):
#     tmp=int(input())
#     Line.append(tmp)
#     largest=max(largest, tmp)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    print(mid, lt, rt)
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

# 3. 뮤직비디오(결정알고리즘)
# 강의 들을 것

# 4. 마구간 정하기
# 강의 들을 것

# 5. 회의실 배정
# 6. 씨름선수
# 7. 창고 정리
# 8. 침몰하는 타이타닉
# 9. 증가수열 만들기
# 10. 역수열