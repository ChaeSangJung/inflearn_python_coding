# 각 자릿수 구하는 함수
def digit_sum(x):
    sum=0
    while x>0:
        t = x%10
        sum = sum + t
        x=x//10      
    return sum

# x= 15232
# print(t, sum, x)
# 1. 2 2 1523
# 2. 3 5 152
# 3. 2 7 15
# 4. 5 12 1
# 5. 1 13 0