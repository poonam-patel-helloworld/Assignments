
import turtle


poonam = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
colours = ("purple","blue","green","yellow","orange")
poonam.speed(5000)

for i in range(150):
    
        poonam.pencolor(colours[i%5])
        poonam.forward(i)
        poonam.right(60)
        poonam.forward(i)
        poonam.right(60)
        poonam.forward(i)
        poonam.right(60)
        poonam.forward(i)
        poonam.right(60)
        poonam.forward(i)
        poonam.right(60)
        poonam.forward(i)
        poonam.right(60)
        
        poonam.penup()
        poonam.left(90)
        poonam.forward(i)
        poonam.pendown()
   
    
turtle.done()

