import random
import turtle
turtle.setup(800, 800)
turtle.bgcolor("black")
turtle.hideturtle()
turtle.tracer(0, 0)
particles = [(0, 0)]
turtle.color("white")
turtle.penup()
turtle.goto(0, 0)
turtle.dot(4)
def is_adjacent(x, y):
    for px, py in particles:
        if abs(x - px) <= 2 and abs(y - py) <= 2:
            return True
    return False
while len(particles) < 300:
    x, y = random.randint(-250, 250), random.randint(-250, 250)
    while True:
        x += random.choice([-1, 1])
        y += random.choice([-1, 1])
        if is_adjacent(x, y):
            particles.append((x, y))
            turtle.goto(x, y)
            turtle.dot(3)
            break
        if abs(x) > 300 or abs(y) > 300:
            x, y = random.randint(-250, 250), random.randint(-250, 250)
    turtle.update()
turtle.done()
