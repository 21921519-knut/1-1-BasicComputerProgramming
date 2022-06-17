#과제 1
'''
sum = 0

for i in range (0, 5 ,1) :
    n = int(input("수를 입력하세요 : "))
    sum = sum + n

print("합 : %d , 평균 : %d" % (sum, sum//5))
'''

#과제 2
'''
floor = int(input("층을 입력하세요 : "))

for i in range(0, floor, 1) :
    print("%s%s" % ((' ' * (floor-i),('*'*(i*2+1)))))
'''
#과제 3
'''
sum = []

for i in range(0, 10, 1) :
    n = int(input("수를 입력하세요 : "))
    if n > 100 :
        n = int(input("다시 입력하세요 : "))
    if n > 50 and n <= 100 :
        sum.append(n)

print(len(sum))
'''

#과제 4
'''
val = []
maxval = int(input("성적을 입력하세요 : "))
m = maxval

for i in range (0, 4, 1) :

    n = int(input("성적을 입력하세요 : "))
    val.append(n)
    if maxval < n :
        maxval = n

sum = val[0] + val[1] + val[2] + val[3] + m

print("총점 : %d ,  가장 큰 점수 : %d" % (sum, maxval))
'''
#과제 4 교수님 편
'''
scores = []
for i in range(0, 5, 1) :
    scores.append(int(input('성적입력 : ')))

maxval = scores[0]
total = scores[0]

for i in scores[1:5] :
    total = total + i
    if maxval < i :
        maxval = i

print(total)
print(maxval)
print('%.1f' % (total / len(scores)) )
'''
