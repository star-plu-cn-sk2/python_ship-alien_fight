#!/usr/bin/env python
import turtle
a = 1
b = 90
turtle.left(90)
for i in range(0,200):
    a = a + 1
    turtle.forward(a)
    turtle.right(b)
    turtle.forward(1)
    turtle.right(b)
    a = a + 1
    turtle.forward(a)
    turtle.left(b)
    turtle.forward(1)
    turtle.left(b)




