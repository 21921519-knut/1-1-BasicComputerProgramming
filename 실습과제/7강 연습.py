'''
version = 1.0

def newVersion(v):
    version = v
    print("My version  =%.1f"% version)
def printVersion() :
    print("Hello, current ver. : %.1f" % version)

printnewVersion()
newVersion(1.5)
printnewVersion()
'''
'''
def avg(k,e,m=50) :
    sum = k + e + m
    avg = s/3

    return a
    #return (k+e+m)//3

print(avg(90,85,80))

print(avg(99,88))
'''
'''
def calsum(*data) :
    sum = 0
    for i in data :
        sum += i

    return sum

def calavg(*data) :
    sum = 0
    for i in data :
        sum += i

    return sum / len(data)

print(calsum(1,2,3,4,5))
print(calavg(1,2,3,4,5))
'''

import random
for i in range(0,5,1) :
    print(random.randrange(5,11))

for i in range(0,5,1) :
    print(random.random())
