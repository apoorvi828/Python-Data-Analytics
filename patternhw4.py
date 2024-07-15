# octagon but with a loop
from turtle import *
speed('fast')
r = getscreen()
d = Turtle()

s  = 8
t = 100
for i in range(s):
    fd(t)
    lt(360/s)
mainloop()
