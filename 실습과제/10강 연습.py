'''
class score :
    point = 0 #속성
    def get(self):
        return self.point

    def set(self,p):
        self.point = p

#-----------------------------

lee = score()
kim = score()

lee.set(88)
kim.set(99)

print(lee.get())
'''
'''
from tkinter import *

win = Tk()

win.title('The first')
win.geometry('200x150')

lb = Label(win, text='Welcome')
lb.pack()

win.mainloop()
'''

class score :
    point = 0 #속성
    def __init__(self,o=-99):
        self.point = o
        
    def get(self):
        return self.point

    def set(self,p):
        self.point = p

class telephoneMGR :
    name = ' '
    #name = None
    phone = ' '

    def setName(self,n):
        self.name = n
    def setPhone(self,p):
        self.phone = p
        
    def getName(self):
        return self.name
    def getPhone(self):
        return self.phone

