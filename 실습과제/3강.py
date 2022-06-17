#과제 1

integer = int(input("수를 입력하세요. : "))
A = integer % 2

if A == 1 :
    print("홀수입니다.")
else :
    print("짝수입니다.")

#과제 2

B = str(input("열 문자 이하의 문자열을 입력하시오 : "))
if len(B) > 10 :
    B = str(input("다시 입력하시오 : "))
print(":%-s %s %-s:" % ((' ' * (len(B) // 2)) , B, (' ' * (len(B) // 2))))

#과제 3
    
name = str(input("이름 : "))
korean = int(input("국어 성적 : "))
english = int(input("영어 성적 : "))
math = int(input("수학 성적 : "))
sum = korean + english + math
avge = sum//3
namelen = len(name)

if avge >= 60 :
    C = "PASS"
else :
    C = "FAIL"

print("%s %s %s" % (' ' * 10, "SCORE", ' ' * 10))
print("%s %s" % ('-' * 20, '-' * 4))
print('%-20s %-s' % (( ' ' * (int ((20 - len(name)) / 2) ) + name), str(C)))
print("%s %s" % ('-' * 20, '-' * 4))



