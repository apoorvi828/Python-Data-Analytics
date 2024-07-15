# concentric circles

from turtle import *
s = Screen() 
s.setup(1000,700) #change screen size using x and y pixels
colors = ['purple', 'blue']
pencolor('green')
pensize(5)
for i in range(6,0,-1):
    penup()  # move pen up from screen
    setpos(0,-20*i)  # move to a position on y-axis
    pendown()  # put pen down from screen
    fillcolor(colors[i % 2])
    begin_fill()
    circle(20*i)  # create circle with different radius because i changes every turn of loop 
    end_fill()
mainloop()