n = 5
word = ['big', 'good', 'sky', 'blue', 'mouse', 'sky', 'good', 'mouse', 'big']
p=dict()

for i in range(n):
  p[word[i]] = 1

for j in range(n,len(word)):
  p[word[j]] = 0

for key, val in p.items():
  if val == 1:
    print(key)
    break


import sys
sys.stdin=open("input.txt", "r")
n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
for key, val in p.items():
    if val==1:
        print(key)
        break



딕셔너리(https://wikidocs.net/16)
1. 기본 딕셔너리의 모습
{Key1:Value1, Key2:Value2, Key3:Value3, ...}
a = {1: 'hi'}
a = { 'a': [1,2,3]}

2. Key 리스트 만들기(keys)
>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
a.keys()는 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려준다.

3. dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
>>> for k in a.keys():
...    print(k)
...
name
phone
birth

4. dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.

>>> list(a.keys())
['name', 'phone', 'birth']

5. Value 리스트 만들기(values)
>>> a.values()
dict_values(['pey', '0119993323', '1118'])
Key를 얻는 것과 마찬가지 방법으로 Value만 얻고 싶다면 values 함수를 사용하면 된다. values 함수를 호출하면 dict_values 객체를 돌려준다.

6. key, Value 쌍 얻기(items)
>>> a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다. dict_values 객체와 dict_items 객체 역시 dict_keys 객체와 마찬가지로 리스트를 사용하는 것과 동일하게 사용할 수 있다.

7. Key: Value 쌍 모두 지우기(clear)
>>> a.clear()
>>> a
{}
clear 함수는 딕셔너리 안의 모든 요소를 삭제한다. 빈 리스트를 [ ], 빈 튜플을 ( )로 표현하는 것과 마찬가지로 빈 딕셔너리도 { }로 표현한다.

8. Key로 Value얻기(get)
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'0119993323'

9. 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> 'name' in a
True
>>> 'email' in a
False