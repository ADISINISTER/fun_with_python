import turtle as tur
import colorsys as cs
tur.setup(600,600)
tur.tracer(10)
tur.width(4)
tur.bgcolor("black")
def square(x):
    for i in range(3):
        tur.forward(x)
        tur.left(90)
    tur.forward(x)
for j in range(20):
    for i in range(10):
        tur.color(cs.hsv_to_rgb(i/10,1-j/20,0.9))
        tur.right(135)
        square(200-j*4)
        tur.right(135)
        tur.circle(50,36)
tur.hideturtle()
tur.done()
