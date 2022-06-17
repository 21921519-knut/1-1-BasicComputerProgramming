#과제 1
'''
Aoa = ['설현', '초아', '지민', '유나', '유경', '혜정', '민아', '찬미']
print(Aoa[2])
print(Aoa[-2])
print(Aoa[0:1])
print(Aoa[6:])
print(Aoa[:])
'''
#과제 2
'''
strs = 'Hong is my friends.'
items = strs.split()
print(items)

for item in items :
    print(item)

exprs = '4 5 3 + *'
items = exprs.split()

for item in items :
    print(item)
'''
#과제 3
'''
oprs = ('+' , '-' , '*' , '/')
exprs = '4 5 3 + *''
items = exprs.split()

for item in items :
    if oprs.count(item) == True :
        print(item, ' : 연산자')
    else :
        print(item, ' : 정수')
'''
#과제 4
'''
data = []

flag = True

while flag :
    item = int(input("수를 입력하세요 : "))
    if item == -1 :
        flag = False
    else :
        data.append(item)

for i in range(0, len(data), 1):
    print(data.pop())
'''
#과제 5
'''
stack = []
ops = ('+' , '-' , '*' , '/')
def isOperator(item) :
    return ops.count(item) == 1

def calc(n1,op,n2) :
    what = ops.index(op)
    rv = 0
    if what == 0 :
        rv = n1 + n2
    elif what == 1 :
        rv = n1 - n2
    elif what == 2 :
        rv = n1 * n2
    elif what == 3 :
        rv = n1 / n2

    return rv

exprs = '4 5 3 + *'
items = exprs.split()

for item in items :
    if isOperator(item) :
        stack.append(calc(stack.pop(), item,  stack.pop()))
    else :
        stack.append(int(item))

print('결과는 = ', stack.pop())
'''
#과제 6
'''
name = str(input("이름을 입력하시오 : "))
kor = int(input("국어 점수 : "))
eng = int(input("영어 점수 : "))
mat = int(input("수학 점수 : "))

avg = int((kor + eng + mat) / 3)

print("%-20s : %s" % (name, ('*' * (avg // 10))))
'''





