import turtle
import math

GRAVITY = 9.81
VELOCITY = 75

screen = turtle.Screen()
screen.title("Ballistic Simulation")
screen.setup(width=800, height=600)

cannon = turtle.Turtle()
cannon.shape("square")
cannon.shapesize(1, 2)
cannon.penup()
cannon.goto(-350, -250)
cannon.setheading(45)

def aim_up():
    if cannon.heading() < 90:
        cannon.setheading(cannon.heading() + 5)

def aim_down():
    if cannon.heading() > 0:
        cannon.setheading(cannon.heading() - 5)

def fire_projectile(x, y):
    projectile = turtle.Turtle()
    projectile.hideturtle()
    projectile.color("red")
    projectile.shape("circle")
    projectile.penup()
    
    projectile.goto(-350, -250)
    angle = math.radians(cannon.heading())
    vx = VELOCITY * math.cos(angle)
    vy = VELOCITY * math.sin(angle)
    projectile.showturtle()
    time = 0
    while projectile.ycor() >= -250:
        projectile.goto(-350 + vx * time, -250 + vy * time - 0.5 * GRAVITY * time**2)
        time += 0.1

    projectile.hideturtle()

screen.listen()
screen.onkey(aim_up, "Up")
screen.onkey(aim_down, "Down")
cannon.onclick(fire_projectile)

screen.mainloop()
