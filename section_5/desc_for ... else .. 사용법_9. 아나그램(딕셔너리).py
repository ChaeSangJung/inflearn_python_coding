import sys
sys.stdin=open("input.txt", "r")
a=input()
b=input()
str1=dict()
str2=dict()
for x in a:
    str1[x]=str1.get(x, 0)+1
for x in b:
    str2[x]=str2.get(x, 0)+1

for i in str1.keys():
    if i in str2.keys():
        if str1[i]!=str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")



<개선된 코드>
import sys
#sys.stdin=open("in1.txt", "r")
a=input()
b=input()
sH=dict()
for x in a:
    sH[x]=sH.get(x, 0)+1
for x in b:
    sH[x]=sH.get(x, 0)-1

for x in a:
    if(sH.get(x)>0):
        print("NO")
        break;
else:
    print("YES")


파이썬, for ... else .. 사용법
for문을 사용하다보면, 루프 중간에 break 문으로 빠져나오는 경우들이 있는데,
이게 break문이 걸려서 빠져나가는지 아닌지를 판단이 필요한 경우가 있습니다.

보통은  flag등을 둬서, 처리하는게 기존의 방식이라면,
for문과 같은 레벨에 else를 둬서 break없이 빠져나온 경우를 처리하는 방법입니다.

for x in range(4):
  if x == 2:
    print ('loop out')
    break
else:
  print ('loop end')


위 예제의 경우는 x =2 에서 루프를 빠져나오기때문에, else문이 실행이 되지 않고
'loop out' 이 출력이 되고,

for x in range(4):
  if x == 5:
    print ('loop out')
    break
else:
  print ('loop end')

  위 예제의 경우는 x =5 에서 루프를 빠져나오기때문에 break에 걸린 것이 아니기 때문에 else문이 실행되어
'loop end' 이 출력

다른 풀이

from collections import Counter

a = Counter(a)
b = Counter(b)

for i in a.keys():
  if i in b.keys():
    if a[i] != b[i]:
      print('NO')
      break
  else:
    print('NO2')
    break

else:
  print('YES')



a = 'AbaAeCe'
b = 'baeeACA'

a = Counter(a)
b = Counter(b)

for i in b.keys():  
  a[i] = a[i] - b[i]
  
for i in a.keys():
  if a[i] > 0 :
    print('NO')
    break

else:
  print('YES')