import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
cnt=0
while True:
    cur=Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break

# any : 조건중 하나라도 맞으면 True를 리턴한다.
# print(any([False, False, False, False])) 
# > False
# print(any([False, True, False, False])) 
# > True

# all : 조건이 전부 True면 True를 리턴하고, 하나라도 틀릴 경우 False를 리턴한다.
# print (all([True, True, True, True])) 
# > True
# print (all([False, True, True, False])) 
# > False

# 파이썬에서는 빈 값, 0, None은 False로 인식한다.

n=6
m=0
arr = [60, 60, 90, 60, 60, 60]

deque([(0, 60), (1, 60), (2, 90), (3, 60), (4, 60), (5, 60)])
cnt = 0

while
    cur=Q.popleft() 
        # cur = (0, 60)
        # Q = [(1, 60), (2, 90), (3, 60), (4, 60), (5, 60)]
    if any(cur[1]<x[1] for x in Q): ture
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:90 true
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:60 false

        Q.append(cur) Q = [(1, 60), (2, 90), (3, 60), (4, 60), (5, 60), (0, 60)]
    
    cur=Q.popleft() 
        # cur = (1, 60)
        # Q = [(2, 90), (3, 60), (4, 60), (5, 60), (0, 60)]
    if any(cur[1]<x[1] for x in Q): true
        cur[1]:60 < x[1]:90 true
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:60 false
        cur[1]:60 < x[1]:60 false

        Q.append(cur) Q = [(2, 90), (3, 60), (4, 60), (5, 60), (0, 60), (1, 60)]
    
    cur=Q.popleft() 
        # cur = (2, 90)
        # Q = [(3, 60), (4, 60), (5, 60), (0, 60), (1, 60)]
    if any(cur[1]<x[1] for x in Q) : false
        cur[1]:90 < x[1]:60 false
        cur[1]:90 < x[1]:60 false
        cur[1]:90 < x[1]:60 false
        cur[1]:90 < x[1]:60 false
        cur[1]:90 < x[1]:60 false
    else:
        cnt = 1
        if cur[0] 2 ==m 0: false
    
    cur=Q.popleft() 
        # cur = (3, 60)
        # Q = [(4, 60), (5, 60), (0, 60), (1, 60)]
        if any(cur[1]<x[1] for x in Q): false
    else:
        cnt = 2
        if cur[0] 3 ==m 0: false

    cur=Q.popleft() 
        # cur = (4, 60)
        # Q = [(5, 60), (0, 60), (1, 60)]
        if any(cur[1]<x[1] for x in Q): false
    else:
        cnt = 3
        if cur[0] 4 ==m 0: false

    cur=Q.popleft() 
        # cur = (5, 60)
        # Q = [(0, 60), (1, 60)]
        if any(cur[1]<x[1] for x in Q): false
    else:
        cnt = 4
        if cur[0] 5 ==m 0: false
    
    cur=Q.popleft() 
        # cur = (0, 60)
        # Q = [(1, 60)]
        if any(cur[1]<x[1] for x in Q): false
    else:
        cnt = 5
        if cur[0] 0 ==m 0: true
            print(cnt 5)
            break