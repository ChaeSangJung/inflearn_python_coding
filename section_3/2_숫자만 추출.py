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