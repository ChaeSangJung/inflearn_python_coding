import sys
sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
seq=[0]*n
for i in range(n):
    for j in range(n):
        if(a[i]==0 and seq[j]==0):
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1

for x in seq:
    print(x, end=' ')

n=8
a=[5, 3, 4, 0, 2, 1, 1, 0]

n=8
a=[5, 3, 4, 0, 2, 1, 1, 0]
seq = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(n:8):
    i=0
    for j in range(n:8):
        j=0
        if(a[i:0]==0 and seq[j:0]==0): false
        elif seq[j:0]==0:
            a[i:0]= a[i:0]5 - 1 a=['4', 3, 4, 0, 2, 1, 1, 0]
        j=1
        if(a[i:0]==0 and seq[j:1]==0): false
        elif seq[j:1]==0:
            a[i:0]= a[i:0]4 - 1 a=['3', 3, 4, 0, 2, 1, 1, 0]
        j=2
        if(a[i:0]==0 and seq[j:2]==0): false
        elif seq[j:2]==0:
            a[i:0]= a[i:0]3 - 1 a=['2', 3, 4, 0, 2, 1, 1, 0]
        j=3
        if(a[i:0]==0 and seq[j:3]==0): false
        elif seq[j:3]==0:
            a[i:0]= a[i:0]2 - 1 a=['1', 3, 4, 0, 2, 1, 1, 0]
        j=4
        if(a[i:0]==0 and seq[j:4]==0): false
        elif seq[j:4]==0:
            a[i:0]= a[i:0]1 - 1 a=['0', 3, 4, 0, 2, 1, 1, 0]
        j=5
        if(a[i:0]==0 and seq[j:5]==0): true
            seq[j:5]=i:0+1, seq = [0, 0, 0, 0, 0, '1', 0, 0]
            break
    i=1
    for j in range(n:8):
        j=0
        if(a[i:1]==0 and seq[j:0]==0): false
        elif seq[j:0]==0:
            a[i:1]= a[i:1]3 - 1 a=[0, '2', 4, 0, 2, 1, 1, 0]