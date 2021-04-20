n=5
a= [
  [10, 13, 10, 12, 15],
  [12, 39, 30, 23, 11],
  [11, 25, 50, 53, 15],
  [19, 27, 29, 37, 27],
  [19, 13, 30, 13, 19]
]
res=0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)

s=2, e=2
i=0
range(2, 2+1)
  res = a[0][2]
  i=0 < n//2 => s=1, e=3

i=1
range(1, 3+1)
  res = a[1][1] + a[1][2] + a[1][3]
  i=0 < n//2 => s=0, e=4

i=2
range(0, 4+1)
  res = a[2][0] + a[2][1] + a[2][2] + a[2][3] + a[2][4]
  else s = 1, e = 3
i=3
range(1, 3+1)
  res = a[3][1] + a[3][2] + a[3][3]
  else s = 2, e = 2
i=4
range(2, 2+1)
  res = a[4][2]
  else s = 3, e = 1