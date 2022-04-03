from turtle import *
color('red', 'yellow')
n = 36
begin_fill()
while n == 36:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
speed(0)
end_fill()
done()
