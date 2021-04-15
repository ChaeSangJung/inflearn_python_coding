lt = 1
rt = Line[n 5-1] 9

while lt 1<=rt 9
    mid=(lt 1+rt 9)//2 5
    Count(5):
        cnt=1
        ep=Line[0] 1
        for i in range(1, n):
            if Line[i 0] 1-ep 1>=len 5:
            if Line[i 1] 2-ep 1>=len 5:
            if Line[i 2] 4-ep 1>=len 5:
            if Line[i 3] 8-ep 1>=len 5:
                cnt 2+=1
                ep=Line[i 3] 8
            if Line[i 4] 9-ep 8>=len 5:
        cnt = 2
        if Count(mid) 2 >=c 3:
        else:
            rt 4 = mid 5 -1 
            # 범위를 큰수에서 줄여라 3개를 넣어야 하는데 2개밖에 안되니까

while lt 1<=rt 4
    mid=(lt 1+rt 4)//2 2
    Count(2):
        cnt=1
        ep=Line[0] 1
        for i in range(1, n):
            if Line[i 0] 1-ep 1>=len 2:
            if Line[i 1] 2-ep 1>=len 2:
            if Line[i 2] 4-ep 1>=len 2:
                cnt 2+=1
                ep=Line[i 2] 4
            if Line[i 3] 8-ep 4>=len 2:
                cnt 3+=1
                ep=Line[i 3] 8
            if Line[i 4] 9-ep 8>=len 2:
        cnt = 3
        if Count(mid) 3 >=c 3:
            res 2 = mid 2
            lt 3 = mid 2 + 1
            # 범위를 작은수에서 줄여라 3개를 넣을 수 있는 최댓값을 찾기 위해

while lt 3<=rt 4
    mid = (lt 3+rt 4)//2 3
    Count(3):
        cnt = 1
        ep = line[0] 1
        for i in range(1, n):
            if Line[i 0] 1-ep 1>=len 3:
            if Line[i 1] 2-ep 1>=len 3:
            if Line[i 2] 4-ep 1>=len 3:
                cnt 2 += 1
                ep = Line[2] 4
            if Line[i 3] 8-ep 4>=len 3:
                cnt 2 += 1
                ep = Line[2] 4
            if Line[i 4] 9-ep 8>=len 3:
        cnt = 3
    if Count(mid) 3 >=c 3
        res 3 = mid 3
        lt 4 = mid 3 + 1

while lt 4<=rt 4
    mid = (lt 4+rt 4)//2 4
    Count(4):
        cnt = 1
        ep = line[0] 1
        for i in range(1, n):
            if Line[i 0] 1-ep 1>=len 4:
            if Line[i 1] 2-ep 1>=len 4:
            if Line[i 2] 4-ep 1>=len 4:
            if Line[i 3] 8-ep 1>=len 4:
                cnt 2 += 1
                ep = Line[3] 8
            if Line[i 4] 9-ep 8>=len 4:
        cnt = 2
    if Count(mid) 2 >=c 3
    else:
        rt 3 = mid 4 -1   

while lt 4<=rt 3 : False