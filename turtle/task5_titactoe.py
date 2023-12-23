import turtle

def draw_board():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)

        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.right(90)
        drawer.forward(600)
        drawer.left(90)

def draw_x(x, y):
    drawer.penup()
    drawer.goto(x + 20, y - 20)
    drawer.pendown()
    drawer.goto(x + 180, y - 180)

    drawer.penup()
    drawer.goto(x + 20, y - 180)
    drawer.pendown()
    drawer.goto(x + 180, y - 20)

def draw_o(x, y):
    drawer.penup()
    drawer.goto(x + 100, y - 175)
    drawer.pendown()
    drawer.circle(80)

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return ""

def board_click(x, y):
    global player
    col = int((x + 300) // 200)
    row = int((300 - y) // 200)

    if board[row][col] == "":
        if player == "x":
            draw_x(-300 + 200 * col, 300 - 200 * row)
            board[row][col] = "x"
            player = "o"
        else:
            draw_o(-300 + 200 * col, 300 - 200 * row)
            board[row][col] = "o"
            player = "x"
        winner = check_winner()
        if winner != "":
            print(f"The winner is {winner}!")
            turtle.bye()

screen = turtle.Screen()
screen.title("Tic-Tac-Toe")
screen.setup(width=600, height=600)

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

draw_board()

board = [["" for _ in range(3)] for _ in range(3)]

player = screen.textinput("Tic-Tac-Toe", "Who goes first? x/o: ")

screen.onclick(board_click)

turtle.done()

