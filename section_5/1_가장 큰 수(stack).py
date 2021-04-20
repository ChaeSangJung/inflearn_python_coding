5276823 3
3의 숫자를 제거하고 가장 큰 수

5276823 순서유지하면서 큰 수
앞에 있는 숫자 중에서 자기보다 작은 수는 지운다.

5'(7보다 작으니까 지우고)''2(7보다 작으니까 지우고)' 7 6'(8보다 작으니까 지우고)'823

Last In First Out

import sys
sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)

num = 5276823
m = 3
num=[5,2,7,6,8,2,3]
stack=[]
for x in num:
    x = 5 m=3 stack=[]
    stack.append(x :5) stack=[5]
    
    x = 2 m=3 stack=[5]
    while stack:true and m:3>0:true and stack[-1]:5<x:2 false:
    stack.append(x :2) stack=[5,2]
    
    x = 7 m=3 stack=[5,2]
    while stack:true and m:3>0:true and stack[-1]:2<x:7 true:
        stack.pop() stack=[5]
        m-=1 : 2
    while stack:true and m:2>0:true and stack[-1]:5<x:7 true:
        stack.pop() stack=[]
        m-=1 : 1
    while stack:false and m:2>0:true and stack[-1]:null<x:7 false:
    stack.append(x :7) stack=[7]

    x = 6 m=1 stack=[7]
    while stack:true and m:1>0:true and stack[-1]:7<x:6 false:
    stack.append(x :6) stack=[7,6]

    x = 8 m=1 stack=[7,6]
    while stack:true and m:1>0:true and stack[-1]:6<x:8 true:
        stack.pop() stack=[7]
        m-=1 : 0
    while stack:true and m:0>0:false and stack[-1]:7<x:8 true:
    stack.append(x :6) stack=[7,8]

    x = 2 m=0 stack=[7,8]
    while stack:true and m:0>0:false and stack[-1]:7<x:8 true:
    stack.append(x :2) stack=[7,8,2]

    x = 3 m=0 stack=[7,8,2]
    while stack:true and m:0>0:false and stack[-1]:2<x:8 true:
    stack.append(x :3) stack=[7,8,2,3]

num = 987654321
m = 6
num = [9,8,7,6,5,4,3,2,1]
stack = []

for x in num:
    x = 9 m=6 stack=[]
    while stack:false and m:6>0 true and stack[-1]:null<x:9 false:
    stack.append(x : 9) stack= [9]

    x = 8 m=6 stack=[]
    while stack:false and m:6>0 true and stack[-1]:null<x:8 false:
    stack.append(x : 8) stack= [9,8]

    .
    .
    .

    x = 2 m=6 stack=[]
    while stack:false and m:6>0 true and stack[-1]:null<x:2 false:
    stack.append(x : 2) stack= [9,8,7,6,5,4,3,2]

    x = 1 m=6 stack=[]
    while stack:false and m:6>0 true and stack[-1]:null<x:1 false:
    stack.append(x : 2) stack= [9,8,7,6,5,4,3,2,1]