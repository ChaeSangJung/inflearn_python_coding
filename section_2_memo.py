# 8.뒤집은 소수
# 수 뒤집기
def reverse(x):
    res=0
    while x>0:
        t=x%10
        # 나머지 값을 10단위 100단위로 순차적으로 올려준다.
        res=res*10+t
        x=x//10
    return res

# 9. 주사위 게임
# map()
# https://dojang.io/mod/page/view.php?id=2286
# map은 리스트의 요소를 지정된 함수로 처리해주는 함수
# map은 원본 리스트를 변경하지 않고 새 리스트를 생성
# list(map(함수, 리스트))
# tuple(map(함수, 튜플))
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
# [1, 2, 3, 4]
b = list(map(str, range(10)))
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']