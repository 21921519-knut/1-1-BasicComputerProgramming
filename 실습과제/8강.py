#과제 1
'''
a = open('i100.dat', 'r')
contents = a.read().split()
b = 0
for content in contents:
    if b == 0:
        Min = content
        Max = content
    b = b + 1
    if Min > content:
        Min = content
    if Max < content:
        Max = content
print("최댓값은 " + Max + "입니다.")
print("최솟값은 " + Min + "입니다.")
a.close()
'''
#과제 2
'''
import pickle
a = open('i100.bin', 'rb')
number = []
b = 0
for i in range(0,100,1):
    number.append(pickle.load(a))
for numbers in number:
    if b == 0:
        Max = numbers
        Min = numbers
    b = b + 1
    if Max < numbers:
        Max = numbers
    if Min > numbers:
        Min = numbers
print("최댓값은 ", Max, "입니다.")
print("최솟값은 ", Min, "입니다.")
a.close()

'''
#과제 3
'''         
import pickle

contents=open('i100.bin','rb')

num=[]
p = -1
for i in range(0,100,1) :
    num.append(pickle.load(contents))

find=int(input('찾을 값을 입력 : '))

for i in range(0, 100, 1) :
    if num[i] == find :
        p = i + 1
        break

if p == -1:
    print(find, "이(가) 파일에 없습니다.")
else:
    print(find,"이(가) ", p, "번째에 저장되어 있습니다.")

contents.close()

'''
