import turtle as r
r.speed(0)
r.bgcolor('black')
r.pencolor('red')
for a in range(155):
     r.rt(a)
     r.circle(125,a)
     r.fd(a)
     r.rt(90)
r.done()
r.exitonclick()
