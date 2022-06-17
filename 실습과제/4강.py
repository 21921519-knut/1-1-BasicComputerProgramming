#과제 1
'''
year = int(input('년도를 입력하세요 : '))

if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0 :
    print("윤년입니다.")
else :
    print("윤년이 아닙니다.")
'''

#과제 2
'''
money = int(input("금액을 입력하세요 : "))

A = money // 50000
B = (money-A*50000) // 10000
C = (money-(A*50000+B*10000)) // 5000
D = (money-(A*50000+B*10000+C*5000)) // 1000
E = (money-(A*50000+B*10000+C*5000+D*1000)) // 500
F = (money-(A*50000+B*10000+C*5000+D*1000+E*500)) // 100
G = (money-(A*50000+B*10000+C*5000+D*1000+E*500+F*100)) // 50
H = (money-(A*50000+B*10000+C*5000+D*1000+E*500+F*100+G*50)) // 10

print("5만원 : %s장 1만원 : %s장 5천원 : %s장 1천원 : %s장 5백원 : %s개 백원 : %s개 5십원 : %s개 십원 : %s개" % (A,B,C,D,E,F,G,H))
'''

#과제 3
'''
A = int(input("첫번째 수를 입력하세요 : "))
big = A
B = int(input("두번째 수를 입력하세요 : "))
if big<B :
    big = B
C = int(input("세번째 수를 입력하세요 : "))
if big<C :
    big = C
D = int(input("네번째 수를 입력하세요 : "))
if big<D :
    big = D
E = int(input("다섯번째 수를 입력하세요 : "))
if big<E :
    big = E

print("가장 큰 수는 %s입니다." % (big))
'''

#과제 4
'''
score = int(input("점수를 입력하세요 : "))

if score < 90 :
    if score < 80 :
        if score < 70 :
            if score < 60 :
                if score < 59 :
                    print("F학점 입니다.")
                else :
                    print("E학점 입니다.")
            else :
                print("D학점 입니다.")
        else :
            print("C학점 입니다.")
    else :
        print("B학점 입니다.")
else :
    print("A학점 입니다.")
'''
