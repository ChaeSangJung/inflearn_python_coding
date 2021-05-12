s='()(((()())(())()))(())'
# 보기 좋게 하기 위해, dict형식으로 돌리지 않음
s= [
    (0,'('), (1,')'), (2,'('), (3,'('), (4,'('),
    (5,'('), (6,')'), (7,'('), (8,')'), (9,')'),
    (10,'('), (11,'('), (12,')'), (13,')'), (14,'('),
    (15,')'), (16,')'), (17,')'), (18,'('), (19,'('),
    (20,')'), (21,')')
]
stack=[]
cnt=0
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            cnt+=len(stack)
        else:
            cnt+=1
    print(s[i],stack, cnt)
print(cnt)

for i in range(len(s)):
    i=0
    if s[0]=='(': true
        stack.append(s[i]) stack=['(']
    i=1
    if s[1]=='(': false
    else 
        stack.pop() stack=[]
        if s[0]=='(': true
            cnt+=len(stack) 0 cnt = 0