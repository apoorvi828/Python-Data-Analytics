from turtle import *
speed('fastest')
s = 8
d = 100
for i in range(s):
    fd(d)
    lt(360/s)
    write(i, font=('Times new roman', 13, 'normal'))
    circle(360/s, 90)

mainloop()