'''
lst = [1, 2, True, 3, 4, None, 5, 6]
print(lst)

lst[2] = False
print(lst)

lst[5] = [11, 'good', 12, 'morning']
print(lst)

print(lst[5][1])

lst[5][2] = [3.14, 99.9, 'hong']
print(lst[5][2][2])

print(lst[-2])
'''
'''
def avg(lst) :
    total = 0

    for item in lst :
        total += item

    return total / len(lst)
scores = [77, 99, 89, 100, 85]

print(avg(scores))
'''
'''
def draw(floor) :
    for i in range (0, floor, 1) :
        print('%s%s' % (' ' * (floor - i+1), '*' * (i*2+1)))

level = int(input('층수를 입력하세요 : '))
draw(level)
'''
