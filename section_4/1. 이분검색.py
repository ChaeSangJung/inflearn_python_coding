# 1. 이분검색
n=8 
m=81
a=[23, 87, 65, 12, 57, 32, 99, 81]
a.sort() # a=[12, 23, 32, 57, 65, 81, 87, 99]
print(a)
lt=0
rt=n-1
while lt<=rt:
    mid=(lt+rt)//2    
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1

rt(7) = 8-1
while 0 <= 8-1(7)
    mid:3 = 0+7//2
    elif a[3]:12 < 81
        lt:4 = 3 + 1 

while 4 <= 7
    mid:5 = 4+7//2
    if a[5]:81 = 81
        print(5 + 1)

answer is 6