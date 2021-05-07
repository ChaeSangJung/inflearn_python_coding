1. 재귀함수란(이진수출력)
import sys
sys.stdin=open("input.txt", "r")
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2) # stack에 귀환 주소로 저장
        #D(0),D(1),D(2),D(3)... 순으로 LIFO 순으로 작동
        print(x%2, end='')

n=int(input())
DFS(n)
