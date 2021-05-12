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

maxx = 9 # dvd에 노래를 잘라서 담을 수 없기에 최소 길이는 노래 중에서 제일 긴 걸로 정한다.
lt=maxx 9 
rt=sum(Music) 45
res=0

while lt 9 <=rt 45:
    mid=(lt 9+rt 45)//2 27
    Count(27):
        for x in Music [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if sum 0 + 1 + 2 + 3 + 4 + 5 + 6 +7 > 27
                cnt 2 += 1
                sum = x 7
        if sum 7 + 8 + 9 > 27
        
        cnt = 2
                
    if mid 27>=maxx 9 and Count(mid) 2 <=m 3: # 3개에 미치지 못했기에 더 줄여라, 27이후부터는 버려라
        res 27 = mid 27
        rt 26 = mid 27 -1

while lt 9 <= rt 26:
    mid = (lt 9 + rt 26)//2 17
    Count(17):
        for x in Music [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if sum 0 + 1+2+3+4+5+6> 17
                count 2 +=1
                sum = x 6
            if sum 6 + 7 +8 > 17
                count 3 +=1
                sum = 8
            else sum 8 +9
        cnt = 3
    
    if mid 17>=maxx 9 and Count(mid) 3 <=m 3: 
        # 더 줄여 보자, 17이후부터는 버려라
        res 17 = mid 17
        rt 16 = mid 17 -1

while lt 9 <= rt 16:
    mid = (lt 9 + rt 16)//2 12
    Count(12):
        for x in Music [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if sum 0 +1+2+3+4+5> 12
                cnt 2 += 1
                sum = x 5
            if sum 5 +6+7> 12
                cnt 2 += 1
                sum = x 7
            if sum 7 +8>12
                cnt 3 += 1
                sum = x 8
            if sum 8 +9>12
                cnt 4 += 1
                sum = x 9
        cnt = 4
    if mid 17>=maxx 9 and Count(mid) 4 <=m 3: 
        # 너무 작다, 왼쪽 최솟값 설정을 올려라.
        else
            lt 18 = 17 +1

while lt 18 <= rt 16: false