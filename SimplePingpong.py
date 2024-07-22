# Here are the mechanics of the game:
    #To play, control the "right" paddle by using the "UP" and "DOWN" arrow keys.
    #On the other hand, control the "left" paddle by using the "W" key to move up and "S" key to move down.
    #Whoever fails to catch the ball, his/her opponent will earn a point.

import turtle
t = turtle.Turtle()

win = turtle.Screen()
win.title("Simple Ping-Pong")
win.bgcolor("#1e8fd5")
win.setup(width=700, height=600)

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("SCORE BOARD", align="center", font=("Courier", 16, "bold"))

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))

#setting up court
t.penup()
t.goto(-275, 180)
t.pendown()
t.width(4)
t.color("white")
for i in range (2):
    t.fd(550)
    t.rt(90)
    t.fd(350)
    t.rt(90)
t.hideturtle()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-240, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(240, 0)

# Ping-Pong Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

#Scoring System
score_a = 0
score_b = 0

#Paddle Functions
def a_moveup():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

    if paddle_a.ycor() > 120:
        paddle_a.sety(120)

def a_movedown():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

    if paddle_a.ycor() < -120:
        paddle_a.sety(-120)

def b_moveup():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

    if paddle_b.ycor() > 120:
        paddle_b.sety(120)

def b_movedown():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)
    
    if paddle_b.ycor() < -120:
        paddle_b.sety(-120)

#Paddle Controls
win.onkey(a_moveup, "w")
win.onkey(a_movedown, "s")
win.onkey(b_moveup, "Up")
win.onkey(b_movedown, "Down")
win.listen()

#main loop
while True:
    win.update()

    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # checking outside court
    if ball.ycor() > 170:
        ball.sety(170)
        ball.dy *= -1

    if ball.ycor() < -160:
        ball.sety(-160)
        ball.dy *= -1

    if ball.xcor() > 270:
        ball.goto(0, 0)
        ball.dx = 2 #reseting to initial speed
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -270:
        ball.goto(0, 0)
        ball.dx = 2 #reseting to initial speed
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))

    # Collisions
    if (ball.xcor() < -220 and ball.xcor() > -240) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-220)
        ball.dx *= -1
        ball.dx +=1
        
    if (ball.xcor() > 220 and ball.xcor() < 240) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(220)
        ball.dx *= -1
        ball.dx -=1 #speeding up
        
