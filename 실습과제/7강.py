#과제 1
'''
def avg(*data) :
    sum = 0
    for i in data :
        sum += i
        
    avg = sum / len(*data)

    return avg
'''
#과제 2
'''
import myUtil

grade = []

for i in range(0, 5, 1) :

    h = int(input('성적을 입력하세요 : '))
    grade.append(h)

print(myUtil.avg(grade))
'''
#과제 3
'''
from myUtil import *

for i in range(0, 5, 1) :

    h = int(input('정수를 입력하세요 : '))
    push(h)

for i in range(0, len(num), 1):
    print(num.pop())
'''
#과제 4
'''
from myUtil import *

exprs = str(input('문자열을 입력하세요 : '))
item = exprs.split()

for item in exprs :
    if isOperator(item) :
        print(item, ' : 연산자')
    elif item == ' ' :
        continue
    else :
        print(item, ' : 정수')
'''
#과제 5
'''
from myUtil import *

stack = []

exprs = '4 5 3 + *'
items = exprs.split()
for item in items :
    if isOperator(item) :
        stack.append(calc(stack.pop(), item, stack.pop()))
    else :
        stack.append(int(item))

print('결과는 = ', stack.pop())
'''



