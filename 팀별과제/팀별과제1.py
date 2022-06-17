#Canvas 위젯은 GUI에 그림을 그릴때 사용된다.

from tkinter import *

Win = Tk()
draw = Canvas(Win,bg='#4B0082',height=444,width=666)

angleproperty = 60,50,420,280
angle = draw.create_arc(angleproperty, start=0, extent=270, fill='#F08080')
 
draw.pack()
Win.mainloop()
