import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Fidget Spinner")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the fidget spinner
spinner = turtle.Turtle()
spinner.shape("triangle")
spinner.color("red")
spinner.speed(-10)
spinner.shapesize(20)
turtle.delay(100)

# Animation loop
while True:
    spinner.right(1)
    screen.update()

# Close the screen on click
screen.exitonclick()