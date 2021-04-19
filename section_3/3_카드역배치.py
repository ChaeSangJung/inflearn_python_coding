import sys
sys.stdin=open('input/txt','r')
a=list(range(21))
for _ in range(10):
    s,e = map(int. input().split())
    for i in range((e-s+1)//2):
        # ex 2~7 2 <-> 7, 3 <-> 6, 4 <-> 5 3times
        a[s+i], a[e-i] = a[e-i], a[s+i]
    a.pop(0) #[0,1,2, ... 19,20] 0 빼야함

    for x in a:
        print(x, end='')

a,b = b,a #swap