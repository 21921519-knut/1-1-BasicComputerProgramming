'''
from tkinter import *
win = Tk()

win.mainloop()
'''
'''
from tkinter import *

win = Tk()
win.title('AC8')
win.geometry('400x500')
win.resizable(width=True,height=True)
lbName=Label(win,text='ddd',font=('Comic Sans','30'),fg='#FFFFFF',bg='#000000',width='5',height='5',anchor=S)
lbTel=Label(win,text='58395793759',font=('Comic Sans','30'))
lbName.pack()
lbTel.pack()
win.mainloop()
'''
'''
from tkinter import *

win = Tk()
win.title('AC8')
win.geometry('900x800')
acac = PhotoImage(file='img.gif')
IbName = Label(win,image=acac)
IbName.pack()

IbText = Label(win, text='그림출력한다',font=('Comic Sans','30'))
IbText.pack()

win.mainloop()
'''
'''
from tkinter import *

def fn():
    print('버튼이 눌려졌습니다')
    exit()

win = Tk()
win.title('AC8')
win.geometry('900x800')
acac = PhotoImage(file='img.gif')
IbName = Button(win,image=acac,command=fn)
IbName.pack()

IbText = Button(win, text='그림출력한다',font=('Comic Sans','30'))
IbText.pack()

win.mainloop()
'''
'''
from tkinter import *

def fn():
    print('버튼이 눌려졌습니다')
    exit()

win = Tk()
win.title('AC8')
win.geometry('900x800')
acac = PhotoImage(file='img.gif')
IbName = Button(win,image=acac,command=fn)
IbName.pack()

IbText = Checkbutton(win, text='그림출력한다',font=('Comic Sans','30'))
IbText.pack()

win.mainloop()
'''
'''
from tkinter import *

def fn():
    print('버튼이 눌려졌습니다')
    exit()
def fn2():
    if isChecked.get() == 0 :
        print('선택되지 않았음')
    else :
        print('선택되었음')

win = Tk()
win.title('AC8')
win.geometry('900x800')
acac = PhotoImage(file='img.gif')
IbName = Button(win,image=acac,command=fn)
IbName.pack()
isChecked = IntVar()

IbText = Checkbutton(win, text='그림출력한다',font=('Comic Sans','30'),\
                     variable=isChecked,command=fn2)
IbText.pack()

win.mainloop()
'''
'''
from tkinter import *

def fn2():
    print('선택한 것은 : ')
    if isChecked.get() == 0 :
        print('선택되지 않았음')
    elif isChecked.get() == 1 :
        print('출력')
    elif isChecked.get() == 2 :
        print('그리기')
    elif isChecked.get() == 3 :
        print('버리기')


win = Tk()
win.title('AC8')
win.geometry('800x400')
isChecked = IntVar()

IbText = Radiobutton(win, text='그림출력한다',font=('Comic Sans','30'),\
                     variable=isChecked,command=fn2, value=1)
IbText.pack()
IbText2 = Radiobutton(win, text='그림그리기한다',font=('Comic Sans','30'),\
                     variable=isChecked,command=fn2, value=2)
IbText2.pack()
IbText3 = Radiobutton(win, text='그림버리기한다',font=('Comic Sans','30'),\
                     variable=isChecked,command=fn2, value=3)
IbText3.pack()

win.mainloop()
'''
'''
from tkinter import *

def fn():
    print('Press', n.get())

window=Tk()
n=IntVar()
lbTest=Checkbutton(window,text='practice',command=fn,variable=n,value=99)
lbTest.pack()
lbTest2=Checkbutton(window,text='ecitcarp',command=fn,variable=n,value=66)
lbTest2.pack()

window.mainloop()
'''
'''
from tkinter import *

def fn():
    print('Press', n.get())

window=Tk()
n=IntVar()
lbTest=Radiobutton(window,text='practice',command=fn,variable=n,value=99)
lbTest.pack()
lbTest2=Radiobutton(window,text='ecitcarp',command=fn,variable=n,value=66)
lbTest2.pack()

window.mainloop()
'''
'''
from tkinter import *

def fn():
    print('입력된것 : ', e.get())

window=Tk()
e=Entry(window)
b=Button(window,text='입력완료',command=fn)
e.pack()
b.pack()

window.mainloop()
'''
'''
from tkinter import *

win=Tk()

b = Label(win,text='입력완료',font=('Comic Sans',25))
c = Label(win,text='입력추가',font=('Comic Sans',25))
d = Label(win,text='입력취소',font=('Comic Sans',25))
e = Label(win,text='출력',font=('Comic Sans',25))
b.pack(side=LEFT,padx=10)
c.pack(side=LEFT,padx=10)
d.pack(side=BOTTOM,pady=20)
e.pack(side=BOTTOM,pady=20)
win.mainloop()
'''

from tkinter import *

top = Tk()

frame1 = Frame(top)
frame2 = Frame(top)

tmp=Label(frame1,text='파일이름 : ')
filename = Entry(frame1,width=10)

tmp.pack(side=LEFT,padx = 10, pady = 10)
filename.pack(side=LEFT,padx = 10, pady = 10)

tmp=Label(frame2,text='파일종류 : ')
tmp.pack(side=LEFT,padx=10,pady=10)

r1=Radiobutton(frame2,text='이진')
r2=Radiobutton(frame2,text='텍스트')

r1.pack(side=LEFT,padx = 10, pady = 10)
r2.pack(side=LEFT,padx = 10, pady = 10)

frame1.pack(side=BOTTOM)
frame2.pack(side=BOTTOM)

top.mainloop()

'''
from tkinter import *

def mhandler(event):
    print('버튼 번호 : ' , event.num)
    print('위치 : ', event.x, '-', event.y)


top = Tk()
top.title('이벤트 처리 실습')
top.geometry('400x350')

top.bind('<Button-1>', mhandler)
top.bind('<B1-Motion>', mhandler)

top.mainloop()
'''
