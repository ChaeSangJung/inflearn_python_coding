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