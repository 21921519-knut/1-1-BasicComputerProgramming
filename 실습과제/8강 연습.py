'''
friends = ['Hong\n' , 'Lee\n' , 'Park\n']

wfile = open('first.txt','w')

print('good morning')
wfile.write('good morning\n')
wfile.writelines(friends)


wfile.close()
'''
'''
rfile = open('first.txt' , 'r')

lst = rfile.readlines()

for item in lst :
    print(item)

rfile.close()
'''
'''
import pickle

wbfile = open('data.dat','wb')

pickle.dump(65,wbfile)
pi = 3.14
pickle.dump(pi,wbfile)
friends = ['hong', 'lee']
pickle.dump(friends,wbfile)
pickle.dump('good morning', wbfile)

wbfile.close()
'''
'''
import pickle

a = open('data.dat', 'rb')

print(pickle.load(a))
print(pickle.load(a))
print(pickle.load(a))
print(pickle.load(a))

a.close()
'''
#과제 2
'''
import pickle

numbers = []

rfile = open('i100.bin','rb')

for i in range(0,100,1) :
    numbers.append(pickle.load(rfile))

rfile.close()

print(numbers)

minValue = numbers[0]
maxValue = numbers[0]

for i in range(1,100,1) :
    if maxValue < numbers[i] :
        maxValue = numbers[i]
    else if minValue > numbers[i] :
        minValue = numbers[i]
'''
#과제 3
'''

n = int(input('찾을 데이터는 : ?'))

flag = False
i = 0

while not flag and i <100 :
    if numbers[i] == n :
        flag = True
    else :
        i = i + 1

if flag :
    print('위치는 ', i, '찾았다.')
else :
    print('없어.')
'''

#컵에 담긴 음료를 바꾸기
'''
import pickle

data = [9,3,2,6,5]

print(data)

tmp = data[0]
data[0] = data[1]
data[1] = tmp

print(data)
'''

#번외과제 : 자료를 크기 순으로 정렬하기
'''
data = [9,3,2,6,5]

print(data)

N = len(data)
for step in range (0,N-1,1) :
    for i in range (0,N-step-1,1) :
        if data[i] > data[i+1] :
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp
            
print(data)
'''
#번외과제 : 자료를 크기 순으로 정렬하기2
'''
import pickle

numbers = []

rfile = open('i100.bin','rb')

for i in range(0,100,1) :
    numbers.append(pickle.load(rfile))

rfile.close()

print(numbers)

N = len(numbers)
for step in range (0,N-1,1) :
    for i in range (0,N-step-1,1) :
        if numbers[i] > numbers[i+1] :
            tmp = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = tmp
print(numbers)
'''
