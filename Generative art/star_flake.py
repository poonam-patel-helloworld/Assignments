
import turtle


poonam = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
colours = ("blue","purple","red","orange","yellow")
poonam.speed(2000)

for i in range(100):
    
        poonam.pencolor(colours[i%5])
    
        poonam.forward(30+i)
        poonam.right(144)
        poonam.forward(30+i)
        poonam.left(72)
        poonam.forward(30+i)
        poonam.right(144)
        poonam.forward(30+i)
        poonam.left(72)
        poonam.forward(30+i)
        poonam.right(144)
        poonam.forward(30+i)
        poonam.left(72)
        poonam.forward(30+i)
        poonam.right(144)
        poonam.forward(30+i)
        poonam.left(72)
        poonam.forward(30+i)
        poonam.right(144)
        poonam.forward(30+i)
        
        poonam.penup()
        poonam.left(108)
        poonam.forward(30)
        poonam.pendown()
   
    
turtle.done()

