import sys
sys.stdin=open("input.txt", "r")
L=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort() # sort 후
for _ in range(m): #m번을 한다.
    a[0]+=1 # 제일 작은 것에 1을 더하고
    a[L-1]-=1 # 제일 큰 것에 1을 빼고
    a.sort() # 다시 sort를 한다.

print(a[L-1]-a[0]) # 차이를 구한다.

