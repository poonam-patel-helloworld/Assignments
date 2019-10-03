
import turtle


poonam = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
colours = ("red", "orange", "green", "blue","purple")
poonam.speed(1000)

for i in range(40):
    
        poonam.pencolor(colours[i%5])
    
        poonam.forward(180+i)
        poonam.right(144)
        poonam.forward(180+i)
        poonam.left(72)
        poonam.forward(180+i)
        poonam.right(144)
        poonam.forward(180+i)
        poonam.left(72)
        poonam.forward(180+i)
        poonam.right(144)
        poonam.forward(180+i)
        poonam.left(72)
        poonam.forward(180+i)
        poonam.right(144)
        poonam.forward(180+i)
        poonam.left(72)
        poonam.forward(180+i)
        poonam.right(144)
        poonam.forward(180+i)
        poonam.penup()
        poonam.forward(i+ i*2)
        poonam.pendown()
   
    
turtle.done()

