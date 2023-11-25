
# ------------------------------------------------------
# ----------------This Python code uses the Turtle module
# to create a visual representation of the Kenyan flag.
# It draws the flag's colors, geometric shapes, cultural symbols
# like shields and spears, and includes text descriptions explaining
# the symbolism behind each element. Users can interact with the flag
# by clicking on specific areas to reveal additional information about
# its symbolism----------------------------------------------
# -------------------------------------------------------------------.
# Import necessary functions from the Turtle module
from turtle import*
tracer(False)
speed(0) # Set drawing speed to maximum
setup(1400, 750,0,0) # Set up the window size
screen=Screen()
screen.bgcolor("darkgreen")# Set background color
screen.title("Kenyan Flag") # Set window title

unit = 8 # Define a unit for stamping
# Function to create a pattern using stamps
def pattern(turtle, start, stop, step):
    for x in range(start, stop + 1, step):
        for y in range(start, stop + 1, step):
            turtle.goto(x * unit, y * unit + 100)# Move turtle to specified position
            turtle.stamp()# Stamp the current shape
            turtle.left(45) # Turn left for the next stamp
            turtle.stamp()
# Create and customize box1 (red squares)
box1 = Turtle(shape="square")
box1.shapesize(3)
box1.color("red")
box1.penup()
box1.speed(0)
pattern(box1, -84, 84, 12)# Apply pattern to box1
# Create and customize box2 (gold squares)
box2 = Turtle(shape="square")
box2.shapesize(1.5)
box2.color("gold")
box2.penup()
box2.speed(16)
pattern(box2, -78, 78, 12)# Apply pattern to box2


# ---------------------------------Function to draw rectangles-----------------
# This function is used to create a fill colored box that I have used it many times..
def boxes(x, y, w, h, fcolor, pcolor):
    # Customize pen and fill colors
    pencolor(pcolor)
    setheading(0)
    penup()
    # Fill the rectangle with specified color
    begin_fill()
    fillcolor(fcolor)
    goto(x,y) # Move turtle to specified position
    pendown()
    # using for loop for rectangle
    for _ in range(2):
        forward(w)
        left(90)
        forward(h)
        left(90)

    end_fill()
# Draw various colored rectangles representing different parts of the flag
boxes(-300, 160, 600, 80, "black","black")
boxes(-300, 140, 600, 20, "white","black")
boxes(-300, 60, 600, 80, "red3","black")
boxes(-300, 40, 600, 20, "white","black")
boxes(-300, -40, 600, 80, "green","black")

# ------------------------------------------------------------------------------------------------------
# --------------------------Function to draw a shield and associated symbols----------------------------
# ------------------------------------------------------------------------------------------------------
def shield():
    setheading(0)
    penup()
    goto(0,22)
    pendown()
    pencolor("red3")
    fillcolor("red3")
    begin_fill()
    left(30)
    circle(90,60)
    circle(90,60)
    left(60)
    circle(90, 60)
    circle(90, 60)
    end_fill()
    def black(x,y):
        pencolor("black")
        fillcolor("black")

        begin_fill()
        penup()
        goto(x,y)
        pendown()
        left(275)
        circle(100, 50)
        left(130)
        circle(100, 50)
        end_fill()
    black(-34, 143)
    setheading(-30)
    black(35, 143)
    penup()
    goto(0,100)
    pendown()
    dot(15,"white")

    def half(x,y,angle):
        fillcolor("white")
        pencolor("white")
        penup()
        goto(x,y)
        pendown()
        setheading(angle)
        begin_fill()
        left(60)
        circle(45, 60)
        left(150)
        forward(47)
        end_fill()

    half(3, 123,0)
    half(-3,167,180)

    half(3, 32, 0)
    half(-3, 76, 180)
# ------------------------------------------------------------------------------------------------------
# --------------------------Function to draw the arrows behind the sheild-------------------------------
# ------------------------------------------------------------------------------------------------------
def spears(x,y,angle):
    pencolor("black")

    penup()
    goto(x,y)
    pendown()
    fillcolor("white")
    begin_fill()
    setheading(angle)
    left(60)
    circle(40,65)
    left(110)
    circle(40, 65)
    right(30)
    forward(165)
    left(90)
    forward(4)
    left(90)
    forward(165)
    end_fill()
spears(-32,158,30)
spears(30,160,-30)
shield()
# ------------------------------------------------------------------------------------------------------
# --------------------------Write text with specified properties at the given coordinates---------------
# ------------------------------------------------------------------------------------------------------
def text(x, y, text, color, size):
    penup()
    goto(x,y)
    pendown()
    pencolor(color)
    write(text,align="center",font=("Elephant",size))

# Draw a border line around the flag at specified coordinates
def border_line(x, y):
    # tracer(True)
    pensize(5)
    penup()
    goto(x,y)
    pendown()
    left(90)
    forward(470)
    left(90)
    forward(620)
    left(90)
    forward(1280)
    left(90)
    forward(620)
    left(90)
    forward(470)
border_line(-170, 325)

boxes(-180,300,350,50,"red","white")
text(0, 300, "Kenyan Flag", "white", 30)
# ------------------------------------------------------------------------------------------------------
# --------------------------Function to handle click event----------------------------------------------
# ------------------------------------------------------------------------------------------------------
def after_click(x, y):
    x1=-300
    x2=300
    y1=-45
    y2=245
    if x1 <= x <= x2 and y1 <= y <= y2:

        boxes(-620, 120, 200, 160, "red", "white")
        text(-520, 220, "White", "white", 30)
        text(-520, 160, "Signifies peace\nand unity", "white", 15)

        boxes(420, 120, 200, 160, "red", "white")
        text(520, 220, "Black", "white", 30)
        text(520, 135, "Represents\nthe people of\nKenya ", "white", 15)

        boxes(-620, -270, 200, 160, "red", "white")
        text(-540, -160, "Red", "white", 30)
        text(-510, -250, "Symbolises \nthe bloodshed\nduring the struggle\nof independence", "white", 13)

        boxes(420, -270, 200, 160, "red", "white")
        text(520, -160, "Green", "white", 30)
        text(525, -250, "Represents the\ncountry's natural\nresources and\nagricultural wealth", "white", 13)

        boxes(-200, -270, 400, 160, "red", "white")
        text(0, -160, "Maasai Shield", "white", 30)
        text(0, -195, "and Spears", "white", 30)
        text(0, -255, "Represents defence\nof freedom and justice", "white", 15)
        done()
onscreenclick(after_click)

hideturtle()# hide the turtle
done() #The window will remained open after the completion
