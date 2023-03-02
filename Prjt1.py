import turtle
loadWindow = turtle.Screen()
turtle.speed(0)
turtle.pencolor('red')
turtle.bgcolor('black')
 
for i in range(100):
          turtle.circle(5*i)
          turtle.circle(-5*i)
          turtle.left(i)
turtle.exitonclick()
