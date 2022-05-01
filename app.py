import turtle

wind = turtle.Screen()
wind.title("Ping Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#madrab1
madrab1=turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(5,1)
madrab1.penup()
madrab1.goto(-360,0)

#madrab2
madrab2=turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("yellow")
madrab2.shapesize(5, 1)
madrab2.penup()
madrab2.goto(360,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=.4
ball.dy=.4

#score
player1 = 0
player2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player1 : {player1}      Player2 : {player2}", align="center", font=("Courier", 24, "normal"))

#functions
def madrab1_up():
    y=madrab1.ycor()
    y+=20
    madrab1.sety(y)

def madrab1_down():
    y=madrab1.ycor()
    y-=20
    madrab1.sety(y)

def madrab2_up():
    y=madrab2.ycor()
    y+=20
    madrab2.sety(y)

def madrab2_down():
    y=madrab2.ycor()
    y-=20
    madrab2.sety(y)

#keyboard bindings
wind.listen()
wind.onkeypress(madrab1_up,"w")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")

#main game loop
while True:
    wind.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        player1 += 1
        score.clear()
        score.write(f"Player1 : {player1}      Player2 : {player2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < - 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player2 += 1
        score.clear()
        score.write(f"Player1 : {player1}      Player2 : {player2}", align="center", font=("Courier", 24, "normal"))

    if (not ball.xcor() <= 350 and ball.xcor() < 360) and (
            not ball.ycor() >= madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(350)
        ball.dx *= -1

    if (not ball.xcor() >= -350 and ball.xcor() > -360) and (
            not ball.ycor() >= madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-350)
        ball.dx *= -1