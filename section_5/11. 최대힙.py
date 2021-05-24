import sys
import heapq as hq
sys.stdin=open("input.txt", "r")
a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        if len(a)==0:
            print(-1)
        else:
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)


import heapq

n = [5,3,6,0,5,0,2,4,0,-1]
heap = []

for i in n:  
  if i == -1:
    break
  if i == 0:
    if len(heap) == 0:
      print(-1)
    else:
      print(heapq.heappop(heap)[1])
  else:
    heapq.heappush(heap, (-i, i))


