import math as m
import turtle as t

def hearta(k):
    return 15*m.sin(k)**3

def heartb(k):
    return 12*m.cos(k)-5*\
        m.cos(2*k)-2*\
            m.cos(3*k)-\
                m.cos(4*k)
t.speed(0)
t.bgcolor("black")
for i in range(100000):
    t.goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        t.color("red")
        t.goto(0,0)
t.done()