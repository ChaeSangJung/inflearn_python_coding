# 1. K번째 약수
# 다른 방법으로...
n=6 
k=1
cnt=0
a=[]
for i in range(1, n+1):
    if n%i==0:
        cnt+=1
        a.append(i)

if(k > len(a)):
  print(-1)
else: 
  print(a[k-1])