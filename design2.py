import turtle

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(140)
t.pensize(2)

color =['red','green','yellow','cyan','orange','skyblue','indigo','violet']

for i in range(0):
    t.pencolor(color[i%8])
    t.circle(190-i,90)
    t.lt(90)
    t.circle(190-i,90)
    t.rt(60)

    