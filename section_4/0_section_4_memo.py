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
# 강의 들을 것 - ok
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0

for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)

# k=4
# n=20
# Line=[802, 743, 457, 539]
# res=0
# largest=802

lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)

# 3. 뮤직비디오(결정알고리즘)
# 강의 들을 것 ok
n=9
m=3
Music= [1, 2, 3, 4, 5, 6, 7, 8, 9]

def Count(capacity):
    cnt=1
    sum=0
    for x in Music:
        if sum+x>capacity:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

# n, m=map(int, input().split())
# Music=list(map(int, input().split()))
maxx=max(Music)
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

maxx=max(Music)
lt=maxx
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

# 4. 마구간 정하기
# 강의 들을 것
import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=1
    ep=Line[0] #end point
    for i in range(1, n):
        if Line[i]-ep>=len:
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

n= 5
c= 3
# Line = [1, 2, 8, 4, 9] 
Line = [1, 2, 4, 8, 9] 

lt=1
rt=Line[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)

# 5. 회의실 배정(그리디)
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
meeting=[]
for i in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b))

n = 5
meeting=[(1, 4),(2, 3),(3, 5),(4, 6),(5, 7)]

meeting.sort(key=lambda x : (x[1], x[0]))
# [(2, 3), (1, 4), (3, 5), (4, 6), (5, 7)]
et=0
cnt=0
new = []
for x, y in meeting:
    if x>=et:
        et=y
        cnt+=1
        new.append((x,y))
print(cnt, new)

# 6. 씨름선수
import sys
sys.stdin=open("input.txt", "r")
n=int(input())
body=[]
for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))

n=5
body=[(172, 67),(183, 65),(180, 70),(170, 72),(181, 60)]

body.sort(reverse=True)
# body.sort(key=lambda x: x[0], reverse=True)
# [(183, 65), (181, 60), (180, 70), (172, 67), (170, 72)]
largest=0
cnt=0
for x, y in body:
    if y>largest:
        largest=y
        cnt+=1
print(cnt)

# 7. 창고 정리
# 8. 침몰하는 타이타닉
# 9. 증가수열 만들기
# 10. 역수열