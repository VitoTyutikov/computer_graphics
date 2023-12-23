import turtle
import time

def create_hand(name, length, width):
    hand = turtle.Turtle()
    hand.shape("square")
    hand.shapesize(length, width, 1)
    hand.color("black" if name != "second" else "red")
    hand.penup()
    hand.goto(0, 0) 
    hand.speed(0)
    return hand

def draw_clock_face():
    clock_face = turtle.Turtle()
    clock_face.speed(0)
    clock_face.hideturtle()
    clock_face.penup()
    clock_face.goto(0, -210)
    clock_face.pendown()
    clock_face.circle(210)

    for hour in range(12):
        clock_face.penup()
        clock_face.goto(0, 0)
        clock_face.setheading(90 - (hour * 30))
        clock_face.forward(190)
        clock_face.pendown()
        clock_face.forward(20)
        clock_face.penup()

def move_hands(hour_hand, minute_hand, second_hand):
    t = time.localtime()
    current_hour = t.tm_hour
    current_minute = t.tm_min
    current_second = t.tm_sec

    hour_hand.setheading(180 - (current_hour % 12 + current_minute // 60) * 30)
    minute_hand.setheading(180 - (current_minute + current_second // 60) * 6)
    second_hand.setheading(180 - current_second * 6)

screen = turtle.Screen()
screen.title("Analog Clock")
screen.tracer(0)

draw_clock_face()

hour_hand = create_hand("hour", 5, 0.5)
minute_hand = create_hand("minute", 7, 0.4)
second_hand = create_hand("second", 9, 0.2)

try:
    while True:
        move_hands(hour_hand, minute_hand, second_hand)
        screen.update()
        time.sleep(1)
except turtle.Terminator:
    print("Clock window closed.")
