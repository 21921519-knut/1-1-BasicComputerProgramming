#과제 1
'''
import pickle
import random

data = open('data.bin','wb')

for i in range(0,100,1) :
    tststr = ''
    for j in range(0,4,1) :
        tststr = tststr + chr(ord('A')+random.randint(0,22))
    pickle.dump(tststr,data)

data.close()
'''
#과제 2
'''
import pickle

data = open('data.bin','rb')
lst = []

for i in range(0,100,1):
    lst.append(pickle.load(data))

N = len(lst)
for step in range (0,N-1,1) :
    for i in range (0,N-step-1,1) :
        if lst[i] > lst[i+1] :
            tmp = lst[i]
            lst[i] = lst[i+1]
            lst[i+1] = tmp
data2 = open('data.srt','wb')
pickle.dump(lst,data2)
data.close()
'''
#과제 3
'''
import pickle
import random

frontlst = []
lst = []
count = 0

data = open('data.srt','rb')

for i in range(0,100,1):
    frontlst.append(pickle.load(data))
    
for i in range(0,100,1) :
    tststr = ''
    for j in range(0,4,1) :
        tststr = tststr + chr(ord('A')+random.randint(0,22))
    lst.append(tststr)

for item in lst:
    if item.find(tststr) :
        print(str.count(tststr), "번 째에 있습니다.")
    else :
        print("없습니다.")
        
data.close()
'''
#과제 4

from tkinter import *
import random
import time
import winsound

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 200)

        # directions
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        
        self.x = starts[0]     # horizontal
        self.y = starts[1]     # vertical

        # speed
        self.speed = 4
        
        # canvas size
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # hitflag
        self.hit_bottom = False

    def hit_paddle(self, pos):
        # get paddle location
        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True

        return False
            

    def draw(self):
        self.canvas.move(self.id, self.x * self.speed, self.y * self.speed)

        # get current position
        # (x0, y0, x1, y1)
        pos = self.canvas.coords(self.id)

        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x *= -1
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)

        # check paddle
        if self.hit_paddle(pos) == True:
            self.y *= -1
            self.increase_speed()
            self.paddle.increase_speed()
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)

        if pos[1] <= 0:
            self.y *= -1
            winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
            
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            winsound.PlaySound('SystemExclamation', winsound.SND_ASYNC)

    def increase_speed(self):
        self.speed *= 1.2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill = color)
        self.canvas.move(self.id, 200, 700)

        # init varibale
        self.x = 0
        self.speed = 6
        self.canvas_width = self.canvas.winfo_width()

        # event handler
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = - self.speed

    def turn_right(self, evt):
        self.x = self.speed

    def increase_speed(self):
        self.speed *= 1.2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    

tk = Tk()
tk.title("Pong Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width = 500, height = 800, bd = 0, highlightthickness = 0)
canvas.pack()

tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')


while True:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()

    tk.update_idletasks()
    tk.update()
    time.sleep(0.03)


