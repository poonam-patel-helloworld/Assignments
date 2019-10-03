
import turtle


poonam = turtle.Turtle()
canvas = turtle.Screen()
canvas.bgcolor("black")
colours = ("blue","purple","orange","red","yellow")
poonam.speed(5000)

for i in range(200):
    
        poonam.pencolor(colours[i%5])
        poonam.pensize(i/30+1)
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

