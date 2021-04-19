n=3
a=[1, 10, 3]
m=5
b=[2, 3, 6, 7, 9]

a.sort()
b.sort()

p1=p2=0
c=[]

while p1<n and p2<m:
    if a[p1]<b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
# a에서 10이라는 숫자때문에 p1 = 2에서 멈췄고(p2는 5까지 다 돌고 while문을 빠져 나왔다.)
# a의 10만 남아 있으니 c[]에 합쳐 줘야 한다. 제일 큰 수이니 뒤에 붙이면 된다.
# [3:] index = 3부터 끝까지
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')