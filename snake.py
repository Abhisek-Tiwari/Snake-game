import turtle
import time
import random

score=0
delay=0.1
high_score=0

#snake lenght
body=[]

#screen
screen=turtle.Screen()
screen.title("Game of Snakes :D")
screen.bgcolor("black")
screen.setup(width=800,height=700)

#snake-head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("yellow")
head.penup()
head.goto(0,0)
head.direction="stop"

#food
food=turtle.Turtle()
food.shape("square")
food.color("white")
food.fillcolor("red")
food.penup()
food.speed(0)
food.ht()
food.goto(100,-200)
food.st()

#score
score_board=turtle.Turtle()
score_board.shape("square")
score_board.fillcolor("grey")
score_board.penup()
score_board.ht()
score_board.goto(0,310)
score_board.write("Current Score: 0  / Highest Score: 0", align="center", font=("Courier", 24, "normal"))

#move
def move_up() :
    if head.direction!="down":
        head.direction="up"
def move_down() :
    if head.direction!="up":
        head.direction="down"
def move_left() :
    if head.direction!="right":
        head.direction="left"
def move_right() :
    if head.direction!="left":
        head.direction="right"
def move_stop():
    head.direction="stop"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
screen.listen()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")
screen.onkey(move_stop,"space")

#game
while True:
    screen.update()
    if head.xcor()>390:
        head.setx(-390)
    if head.xcor()<-390:
        head.setx(390)
    if head.ycor()>340:
        head.sety(-340)
    if head.ycor()<-340:
        head.sety(340)
    #check if snake ate foood    
    if head.distance(food)<20:
        #new food spaw and its location
        x=random.randint(-390,390)
        y=random.randint(-340,340)
        food.goto(x,y)
        #update body
        bodies=turtle.Turtle()
        bodies.speed(0)
        bodies.penup()
        bodies.shape("circle")
        bodies.color("white")
        bodies.fillcolor("blue")
        body.append(bodies)
        #update score
        score+=1
        delay-=0.001
        if score>high_score:
            high_score=score
        score_board.write("Current Score: {}  / Highest Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    #move body
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)
    if len(body)>0:
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
    move()
    #check if snake hit itself
    for bodies in body:
        if bodies.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            
            for bodies in body:
                bodies.ht()
            body.clear()
            
            #reset score
            score= 0
            delay= 0.1
            
            #update scoreboard
            score_board.write("Current Score: {}  / Highest Score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
screen.mainloop()