'''
maxValue = int(input('Number : '))

for i in range(1, 5, 1) :
    n = int(input('Number : '))
    if maxValue < n :
        maxValue = n

print('Maximum : ', maxValue)
'''
'''
for dan in range (2, 10, 1) :
    for i in range (2, 10, 1) :
        print('%d * %d = %d' % (dan, i, (dan*i)))
    print('-' * 20)
'''
'''
nofdata = 1
minvalue = int(input('수를 입력 : '))

while nofdata < 5 :
    nofdata += 1
    n = int(input('수를 입력 : '))
    if n < minvalue :
        n = minvalue

print('가장 작은 수 : %d' % minvalue)
'''
'''
total = 0

while True :
    score = int(input('성적을 입력하세요 : '))
    if score < 0 :
        break
    total += score

print("총점 : %d" % total)
'''
'''
friends = ['Hong', 'kim', 'lee']
print(friends)

for i in range(0, 3, 1) :
    print(friends[i])

print('-' * 10)

friends.append('honggildong')

for n in friends :
    print(n)
'''

scores = []

for i in range(0, 5, 1) :
    n = int(input("성적을 입력하세요 : "))
    scores.append(n)
"""
for i in range(0,5,1) :
    print(scores[i])

for n in scores :
    print(n)
"""
print(len(scores))

for i in range (0,len(scores),1) :
    print(scores[i])



