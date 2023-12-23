import turtle

def draw_fractal_tree(t, branch_length, angle, shrink_factor):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(angle)
        draw_fractal_tree(t, branch_length - shrink_factor, angle, shrink_factor)
        t.left(2 * angle)
        draw_fractal_tree(t, branch_length - shrink_factor, angle, shrink_factor)
        t.right(angle)
        t.backward(branch_length)

screen = turtle.Screen()

t = turtle.Turtle()
turtle.tracer(0, 0)
t.width(2)
t.left(90)
t.up()
t.backward(100)
t.down()


draw_fractal_tree(t, 100, 30, 15)
turtle.update()
screen.exitonclick()