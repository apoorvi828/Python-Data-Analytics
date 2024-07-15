# hexagonal pattern
 
from turtle import *
speed('fastest')
bgcolor('black')
colors = ['red','purple','blue','green','yellow','orange']
for x in range(360):
    pencolor(colors[x % 6]) # select a number for color
    width(x / 100 + 1) # set pen width
    fd(x)
    lt(59) # make a rotation to 59 degree
mainloop()
