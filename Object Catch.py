import turtle
import random

screen = turtle.Screen()
screen.title("Click to Catch!")
screen.setup(width=600, height=600)

obj = turtle.Turtle()
obj.shape("circle")
obj.color("red")
obj.penup()
obj.hideturtle()

score = 0
misses = 0

def show_object():
    global misses
    if misses >= 3:
        print("Game Over! Final Score:", score)
        return
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    obj.goto(x, y)
    obj.showturtle()
    screen.ontimer(next_round, 1200)  

def next_round():
    global misses
    if obj.isvisible():
        obj.hideturtle()
        misses += 1
        print("Missed! Misses:", misses)
    show_object()  

def catch(x, y):
    global score
    if obj.isvisible() and obj.distance(x, y) < 20:
        obj.hideturtle()
        score += 1
        print("Caught! Score:", score)

obj.onclick(catch)

show_object()
screen.mainloop()
