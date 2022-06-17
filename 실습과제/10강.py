#과제 1
'''
class Score :
    point = 0
    id = " "

    def __init__(self,id,p=0):
        self.point = p
        self.id = id

    def set(self,p):
        self.point = p

    def get(self):
        return self.point


kim = Score('1725001')
lee = Score('1725002',88)

print(kim.get())
print(lee.get())
'''
#과제 2
'''
from Score import *

lee = Score('1725001')
kim = Score('1725002',88)

print(lee.get())
print(kim.get())
'''
#과제 3
'''
from Score import *

lee = Score('1725001')
kim = Score('1725002',88)
hong = Score(p=88,id='1725003')

print("이순신 : ", lee.getId())
print("김순대 : ", kim.getId())
print("홍길동 : ", hong.getId())

n = input("학번을 입력하세요 : ")
hong.set(n)

print("이순신 :", lee.getId())
print("김순대 :", kim.getId())
print("홍길동 :", hong.getId())
'''
#과제 4

from Score import *

option = car()

for i in range(0,3,1):
    c = input('차의 색깔 : ')
    p = input('차의 종류 : ')
    h = input('차의 최고속도 : ')

    option.inputcar(c,p,h)

option.printcar()




#과제 5
'''
from Score import *

sm = ScoreMgr()

for i in range(0,3,1):
    id = input('학번을 넣어라 : ')
    p = int(input('점수를 넣어라 : ') )
    
    sm.inputScore(id, p)

print('총점은 =', sm.getTotal() )

i = input('찾을 학번을 입력 : ' )

score = sm.findId(i)

print( '찾은 학생 점수 :', score )
'''
