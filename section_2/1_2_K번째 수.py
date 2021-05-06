# 2. K번째 수
# 강의 들을 것!!
# 안들어도 됨
import sys
sys.stdin=open("input.txt", "r")
T=int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))

n=6
s=2
e=5
k=3
a=[5,2,7,3,8,9]
a=a[s-1:e]
a.sort()
print((1, a[k-1]))