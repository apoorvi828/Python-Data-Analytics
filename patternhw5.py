# colored shapes
from turtle import *
fillcolor('red')
begin_fill()
s = 5
t = 100
for i in range(s):
    fd(t)
    lt(360/s)
end_fill()
fillcolor('yellow')
begin_fill()
circle(50)
end_fill()
mainloop()    