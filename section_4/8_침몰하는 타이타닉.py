import sys
from collections import deque
sys.stdin=open("input.txt", "r")
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p) # 왼쪽에서 오른쪽에서 자유롭게 넣고 뺄 수 있는 것
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)

n=5 
limit=140
p=[90, 50, 70, 100, 60]
p.sort = [50, 60, 70, 90, 100]