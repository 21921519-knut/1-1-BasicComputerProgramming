def avg(data) :
    sum = 0
    for i in data :
        sum = sum + i
    av = sum / len(data)

    return av

num = []

def push(data) :
    num.append(data)

def pop() :
    num.reverse()

oprs = ('+','-','*','/')
def isOperator (item):
    return oprs.count(item) == True

def calc(n1,op,n2) :
    what = oprs.index(op)
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
