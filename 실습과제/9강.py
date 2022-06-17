#틀 만들기
'''
from tkinter import *

top = Tk()

frame1 = Frame(top)
frame2 = Frame(top)
frame3 = Frame(top)
frame4 = Frame(top)

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

tmp=Label(frame3,text='기능 : ')
readbutton = Button(frame3,text='읽기')
tmp.pack(side=LEFT,padx=10,pady=10)
readbutton.pack(side=LEFT,padx = 10, pady = 10)

tmp=Label(frame4,text='내용 : ')
variable = Label(frame4,text=' ')
tmp.pack(side=LEFT,padx=10,pady=10)
variable.pack(side=LEFT,padx = 10, pady = 10)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

top.mainloop()
'''
#과제 1
from tkinter import *

def chk():
    global n
    n = n+1
    label.configure(text='노른수 : '+ str(n))
