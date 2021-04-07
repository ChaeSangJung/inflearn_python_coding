# 1. 회문 문자열 검사

# 2. 숫자만 추출
s="g0en2Ts8eSoft0"
res=0
for x in s:  
  if x.isdecimal():
    res=res*10+int(x)
  print(res)

# 1. res = 0*10 + 2 (2)
# 2. res = 2*10 + 8 (28)
# 3. trd = 28*10 + 0 (280)

cnt=0
for i in range(1, res+1):
  # res를 res길이만큼 구해서 1~res길이의 수로 나누어서 나머지(%)가 0인 숫자가 약수
  if res%i==0:
    cnt+=1
print(cnt)

# 3. 카드역배치
# 강의 들을 것!

# 4. 두 리스트 합치기
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

# 5. 수들의 합
# 강의 들을 것!