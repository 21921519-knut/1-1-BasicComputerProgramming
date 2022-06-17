#문자열
'''
lst = [1,2,3,4,5]
teststr = 'Good \nMorning\n'

print(teststr)
print(teststr[0])
#teststr[0] = 'g'
#print(teststr)
print(len(lst))
print(len(teststr))
'''
#문자열의 함수와 메소드
'''
lst = [1,2,3,4,5]
teststr = 'Good 아침'

print(teststr)
print(teststr.upper())
print(teststr.lower())
print(teststr.title())
'''
#문자열 변경 및 분리
'''
teststr = 'Good 아침'

rstr = teststr.replace('G','g')
sstr = teststr.split()
print(rstr)
print(sstr)
'''
'''
str1 = '*'
str2 = 'morning'
print(str1+str2)
sstr = str1.join(str2)
ssstr = sstr.split('*')
print(ssstr)
'''
#글자 코드 관련 함수

al = 'abcde'
al = al.upper()
ko = '안녕하세요'
for ch in ko :
    print(ord(ch))
print(ord('0'))
if 'good' > 'good ' :
    print('hello')
else :
    print('good morning')

