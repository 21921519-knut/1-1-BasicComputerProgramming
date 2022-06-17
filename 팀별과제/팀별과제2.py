import pickle
from tkinter import *

#데이터 오픈
dataopen = open('data.dat','rb')
#구간마다 각 숫자의 개수
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#예외 처리 : 음수 또는 100 초
error = 0

for i in range(0,1000,1):
    exnum = pickle.load(dataopen)
    if exnum<0:
        error = error + 1
    elif exnum<=10:
        count[0] = count[0] + 1
    elif exnum<=20:
        count[1] = count[1] + 1
    elif exnum<=30:
        count[2] = count[2] + 1
    elif exnum<=40:
        count[3] = count[3] + 1
    elif exnum<=50:
        count[4] = count[4] + 1
    elif exnum<=60:
        count[5] = count[5] + 1
    elif exnum<=70:
        count[6] = count[6] + 1
    elif exnum<=80:
        count[7] = count[7] + 1
    elif exnum<=90:
        count[8] = count[8] + 1
    elif exnum<=100:
        count[9] = count[9] + 1
    elif exnum>100:
        error = error + 1

if error != 0:
    message = Tk()
    message.title("경고")
    err = Label(message, text = '%d개의 비정상 데이터(0 미만의 수 또는 100 초과의 수)가 존재합니다. 파일을 확인해주세요.'%error)
    bu = Button(message, text = '확인', command = message.quit)
    err.pack()
    bu.pack()
    message.mainloop()

max = 0
for bs in count :
    if max < bs:
        max = bs

Win = Tk()
Win.title("출력 결과")
Win.configure(background='white')

gr = Frame(Win)
c0 = Frame(gr)
c1 = Frame(gr)
c2 = Frame(gr)
c3 = Frame(gr)
c4 = Frame(gr)
c5 = Frame(gr)
c6 = Frame(gr)
c7 = Frame(gr)
c8 = Frame(gr)
c9 = Frame(gr)
level1 = Frame(Win)
level2 = Frame(Win)

levelnum0 = Label(level2,text='0~10',font=('Comic Sans','8'))
levelnum1 = Label(level2,text='11~20',font=('Comic Sans','8'))
levelnum2 = Label(level2,text='21~30',font=('Comic Sans','8'))
levelnum3 = Label(level2,text='31~40',font=('Comic Sans','8'))
levelnum4 = Label(level2,text='41~50',font=('Comic Sans','8'))
levelnum5 = Label(level2,text='51~60',font=('Comic Sans','8'))
levelnum6 = Label(level2,text='61~70',font=('Comic Sans','8'))
levelnum7 = Label(level2,text='71~80',font=('Comic Sans','8'))
levelnum8 = Label(level2,text='81~90',font=('Comic Sans','8'))
levelnum9 = Label(level2,text='91~100',font=('Comic Sans','8'))

c0.configure(background='white')
c1.configure(background='white')
c2.configure(background='white')
c3.configure(background='white')
c4.configure(background='white')
c5.configure(background='white')
c6.configure(background='white')
c7.configure(background='white')
c8.configure(background='white')
c9.configure(background='white')

w0 = Canvas(c0, height = count[0], width = 25, bg = 'black')
w1 = Canvas(c1, height = count[1], width = 25, bg = 'black')
w2 = Canvas(c2, height = count[2], width = 25, bg = 'black')
w3 = Canvas(c3, height = count[3], width = 25, bg = 'black')
w4 = Canvas(c4, height = count[4], width = 25, bg = 'black')
w5 = Canvas(c5, height = count[5], width = 25, bg = 'black')
w6 = Canvas(c6, height = count[6], width = 25, bg = 'black')
w7 = Canvas(c7, height = count[7], width = 25, bg = 'black')
w8 = Canvas(c8, height = count[8], width = 25, bg = 'black')
w9 = Canvas(c9, height = count[9], width = 25, bg = 'black')

w0.pack(side = BOTTOM,padx=14)
w1.pack(side = BOTTOM,padx=14)
w2.pack(side = BOTTOM,padx=14)
w3.pack(side = BOTTOM,padx=14)
w4.pack(side = BOTTOM,padx=14)
w5.pack(side = BOTTOM,padx=14)
w6.pack(side = BOTTOM,padx=14)
w7.pack(side = BOTTOM,padx=14)
w8.pack(side = BOTTOM,padx=14)
w9.pack(side = BOTTOM,padx=14)

b0 = Canvas(c0, height = max-count[0], width = 25, bg = 'white')
b1 = Canvas(c1, height = max-count[1], width = 25, bg = 'white')
b2 = Canvas(c2, height = max-count[2], width = 25, bg = 'white')
b3 = Canvas(c3, height = max-count[3], width = 25, bg = 'white')
b4 = Canvas(c4, height = max-count[4], width = 25, bg = 'white')
b5 = Canvas(c5, height = max-count[5], width = 25, bg = 'white')
b6 = Canvas(c6, height = max-count[6], width = 25, bg = 'white')
b7 = Canvas(c7, height = max-count[7], width = 25, bg = 'white')
b8 = Canvas(c8, height = max-count[8], width = 25, bg = 'white')
b9 = Canvas(c9, height = max-count[9], width = 25, bg = 'white')

line = Canvas(level1, height = 5, width = 580, bg = '#FF0000')

b0.pack(side = BOTTOM,padx=14)
b1.pack(side = BOTTOM,padx=14)
b2.pack(side = BOTTOM,padx=14)
b3.pack(side = BOTTOM,padx=14)
b4.pack(side = BOTTOM,padx=14)
b5.pack(side = BOTTOM,padx=14)
b6.pack(side = BOTTOM,padx=14)
b7.pack(side = BOTTOM,padx=14)
b8.pack(side = BOTTOM,padx=14)
b9.pack(side = BOTTOM,padx=14)

c0.pack(side = LEFT)
c1.pack(side = LEFT)
c2.pack(side = LEFT)
c3.pack(side = LEFT)
c4.pack(side = LEFT)
c5.pack(side = LEFT)
c6.pack(side = LEFT)
c7.pack(side = LEFT)
c8.pack(side = LEFT)
c9.pack(side = LEFT)

line.pack()

levelnum0.pack(side=LEFT,padx=13.5)
levelnum1.pack(side=LEFT,padx=7.5)
levelnum2.pack(side=LEFT,padx=13.5)
levelnum3.pack(side=LEFT,padx=7.5)
levelnum4.pack(side=LEFT,padx=13.5)
levelnum5.pack(side=LEFT,padx=7.5)
levelnum6.pack(side=LEFT,padx=10.5)
levelnum7.pack(side=LEFT,padx=10.5)
levelnum8.pack(side=LEFT,padx=10.5)
levelnum9.pack(side=LEFT,padx=9)

b0.pack(side = LEFT,padx=14)
b1.pack(side = LEFT,padx=14)
b2.pack(side = LEFT,padx=14)
b3.pack(side = LEFT,padx=14)
b4.pack(side = LEFT,padx=14)
b5.pack(side = LEFT,padx=14)
b6.pack(side = LEFT,padx=14)
b7.pack(side = LEFT,padx=14)
b8.pack(side = LEFT,padx=14)
b9.pack(side = LEFT,padx=14)

level2.pack(side = BOTTOM)
level1.pack(side = BOTTOM)
gr.pack(side = BOTTOM)

Win.mainloop()
