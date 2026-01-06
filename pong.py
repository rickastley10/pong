import turtle as t

t.setup(900, 900)
t.bgcolor("black")
t.tracer(0, 0)
t.hideturtle()

# Game variables
bx, by = 0, 0
vx, vy = 20, 20
racket1x = -300  # LEFT side of screen
racket1y = 0
racket_width = 10
racket_height = 100

# Colors
t.pencolor("red")
t.color("red")
t.fillcolor("red")

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
    # Draw rectangle
    t.goto(racket1x + racket_width, racket1y)
    t.goto(racket1x + racket_width, racket1y - racket_height)
    t.goto(racket1x, racket1y - racket_height)
    t.goto(racket1x, racket1y)
    t.end_fill()
    t.penup()

def up():
    global racket1y
    if racket1y < 400:  # Don't go off top
        racket1y += 20

def down():
    global racket1y
    if racket1y > -400:  # Don't go off bottom
        racket1y -= 20

t.listen()
t.onkeypress(up, "w")
t.onkeypress(down, "s")

def update_game():
    global bx, by, vx, vy
    
    # Update ball
    bx += vx
    by += vy
    
    # Bounce off walls
    if bx > 440 or bx < -440:
        vx = -vx
    if by > 440 or by < -440:
        vy = -vy
    
    # ===== FIXED COLLISION DETECTION =====
    # Racket edges
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
        
        # Ball hit racket - bounce back!
        vx = abs(vx)  # Make it move RIGHT (positive)
        bx = racket_right + 20  # Move ball to right of racket
    if bx < -310:
        bx = 0
        by = 0
        
    # Draw everything
    t.clear()
    draw_racket()
    draw_ball()
    t.update()
    
    # Next frame
    t.ontimer(update_game, 30)

update_game()
t.mainloop()