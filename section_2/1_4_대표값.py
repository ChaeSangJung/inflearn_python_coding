n=10
a=[45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
ave=sum(a)/n
# 반올림 int(74.3) => 74, int(73.9) => 73
ave=ave+0.5
ave=int(ave)
min=2147000000
for idx, x in enumerate(a):
    # print(idx, ":", x)
    # 0 : 45
    # 1 : 73
    # 2 : 66
    # 3 : 87
    # 4 : 92
    # 5 : 67
    # 6 : 75
    # 7 : 79
    # 8 : 75
    # 9 : 80
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        # 조건을 x>score 로 걸었기 때문에 뒤에 같은 점수가 나와도 번호가 빠른 값이 출력이 됨
        if x>score:
            score=x
            res=idx+1
print(ave, res)

enumerate
리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능을 가집니다.
이 함수는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴합니다.

data = enumerate((1, 2, 3))
print(data, type(data))
0 : 1
1 : 2
2 : 3

for i, value in data:
    print(i, ":", value)
print()
0 : 1
1 : 2
2 : 3

dict1 = {'이름': '한사람', '나이': 33}
data = enumerate(dict1)
for i, key in data:
    print(i, ":", key, dict1[key])
print()
0 : 이름 한사람
1 : 나이 33

data = enumerate("재미있는 파이썬")
for i, value in data:
    print(i, ":", value)
print()
0 : 재
1 : 미
2 : 있
3 : 는
4 :  
5 : 파
6 : 이
7 : 썬
range([strat,] stop [,step])