import turtle as t



t.title("pong")
t.setup(900, 900)
t.bgcolor("black")
t.tracer(0, 0)
t.hideturtle()
t.delay(0)

# To enable, set it to 1
cheats = 0

# Game variables
speed = 20
fps = 30
bx, by = 0, 0
score = 0
vx, vy = speed, speed
racket1x = -300  
racket1y = 0
racket_width = 10
racket_height = 100



t.pencolor("red")
t.color("red")
t.fillcolor("red")

def borders():
    t.pencolor("red")
    t.pensize(3)
    t.goto(400,400)
    t.pendown()
    t.goto(400, -400)
    t.goto(-400, -400)
    t.goto(-400, 400)
    t.goto(400, 400)
    t.penup()
    
    

def draw_ball():
    t.penup()
    t.goto(bx, by - 20)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()



def draw_racket():
    t.penup()
    t.goto(racket1x, racket1y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()

    t.goto(racket1x + racket_width, racket1y)
    t.goto(racket1x + racket_width, racket1y - racket_height)
    t.goto(racket1x, racket1y - racket_height)
    t.goto(racket1x, racket1y)
    t.end_fill()
    t.penup()



def up():
    global racket1y
    if racket1y < 400:  # Don't go off top
        racket1y += 100



def down():
    global racket1y
    if racket1y > -400:  # Don't go off bottom
        racket1y -= 100

def screenclicks(x, y):
    if y > 0:
        up()
    elif y < 0:
        down()

t.listen()

t.onkeypress(up, "w")
t.onkeypress(down, "s")
t.onkeypress(up, "Up")
t.onkeypress(down, "Down")
t.onscreenclick(screenclicks)

def update_game():

    global bx, by, vx, vy, score
    
    # Update ball
    

    bx += vx
    by += vy

    # Bounce off walls
    if bx > 400 or bx < -400:

        vx = -vx


    if by > 400 or by < -400:

        vy = -vy

    racket_left = racket1x
    racket_right = racket1x + racket_width
    racket_top = racket1y
    racket_bottom = racket1y - racket_height

    # Ball edges (radius = 20)
    ball_left = bx - 20
    ball_right = bx + 20
    ball_top = by + 20
    ball_bottom = by - 20
    # Check collision

    if (ball_right >= racket_left and 
        ball_left <= racket_right and
        ball_top >= racket_bottom and
        ball_bottom <= racket_top):
        score += 1
        # Ball hit racket - bounce back!
        vx = abs(vx)  # Make it move RIGHT (positive)
        bx = racket_right + 20  # Move ball to right of racket
    if bx < -320:
        bx = 0
        by = 0
        score = 0
    # Draw everything
    t.clear()
    t.goto(0, 0)
    t.write(score, align="center", font=("Arial", 18, "normal"))
    borders()
    draw_racket()
    draw_ball()
    t.update()
    # Next frame
    t.ontimer(update_game, fps)
    #cheats
    if cheats == 1:
    	if ball_bottom > racket_top:
    		up() 
    	elif ball_top < racket_bottom:
    		down()


update_game()

t.mainloop()


