app.background = 'olive'

# Stores the snake and the height of the most recently added body part.
app.snake = [ ]
app.bodyPartHeight = 30

nest = Group(
    Circle(200, 200, 90, fill=gradient(rgb(100, 69, 19),rgb(80, 69, 50)),
           border=rgb(100, 69, 19), borderWidth=3, opacity=70, dashes=(20, 7)),
    Line(195, 102, 100, 180, fill=rgb(100, 69, 19), lineWidth=3),
    Line(118, 134, 237, 109, fill=rgb(80, 69, 50), lineWidth=3),
    Line(158, 106, 280, 130, fill=rgb(100, 69, 19), lineWidth=3),
    Line(202, 103, 293, 170, fill=rgb(80, 70, 50), lineWidth=3),
    Line(241, 110, 304, 207, fill=rgb(100, 69, 19), lineWidth=3),
    Line(274, 137, 286, 238, fill=rgb(80, 70, 50), lineWidth=3),
    Line(288, 171, 272, 272, fill=rgb(100, 69, 19), lineWidth=3),
    Line(298, 210, 246, 282, fill=rgb(80, 70, 50), lineWidth=3),
    Line(292, 244, 222, 283, fill=rgb(100, 69, 19), lineWidth=3),
    Line(270, 270, 196, 285, fill=rgb(80, 70, 50), lineWidth=3),
    Line(254, 282, 156, 280, fill=rgb(100, 69, 19), lineWidth=3),
    Line(210, 287, 130, 267, fill=rgb(80, 70, 50), lineWidth=3),
    Line(164, 290, 117, 243, fill=rgb(100, 69, 19), lineWidth=3),
    Line(155, 288, 112, 223, fill=rgb(80, 70, 50), lineWidth=3),
    Line(113, 243, 127, 182, fill=rgb(100, 69, 19), lineWidth=3),
    Line(125, 228, 107, 154, fill=rgb(80, 70, 50), lineWidth=3),
    Line(102, 208, 121, 142, fill=rgb(100, 69, 19), lineWidth=3),
    Line(109, 240, 116, 132, fill=rgb(80, 70, 50), lineWidth=3)
    )
nest.width /= 1.2
nest.height /= 1.2

# eggs
Oval(175, 175, 30, 40, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=20)
Oval(200, 190, 30, 35, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=-20)
Oval(230, 220, 30, 40, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=20)
Oval(226, 180, 27, 35, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=-20)
Oval(200, 223, 30, 35, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=-20)
Oval(173, 210, 30, 40, fill=gradient('ivory', 'wheat', start='top'), rotateAngle=20)

# head of the snake
head = Group(
    Polygon(5, 35, 5, 65, 40, 58, 40, 42,
            fill=gradient(rgb(0, 70, 0), 'darkGreen', start='right')),
    Oval(5, 50, 20, 30, fill='darkGreen'),
    Oval(40, 50, 5, 16, fill=rgb(0, 70, 0)),
    Line(40, 50, 45, 50, fill='darkRed'),
    Line(45, 50, 50, 45, fill='darkRed'),
    Line(45, 50, 50, 55, fill='darkRed')
    )
head.dx = 50
head.dy = 0
app.snake.append(head)

def createBodyPart(height):
    # Creates a body part of the snake with the correct size.
    body = Group(
        Polygon(50, 40, 50, 60, 25, 50 + height / 2, 0, 60, 0, 40,
                25, 50 - height / 2,
                fill=gradient(rgb(0, 70, 0), 'darkGreen', start='left')),
        )
    stripe = Line(body.centerX, body.top, body.centerX, body.bottom,
                  fill=gradient('oliveDrab', 'gray'), lineWidth=3)
    body.add(stripe)
    body.dx = 50
    body.dy = 0
    
    # Adds the new body part to the end of the snake.
    app.snake.append(body)

def setValues(part, newX, newY, angle, newDx, newDy):
    part.rotateAngle = angle
    part.centerX = newX
    part.centerY = newY
    part.dx = newDx
    part.dy = newDy

def changeValues(part):
    # Changes the property of the parts to their new values.
    if (part.centerX > 370):
        setValues(part, 340, 75, 90, 0, 50)
    if (part.centerY > 370):
        setValues(part, 315, 340, 180, -50, 0)
    if (part.centerX < 50):
        setValues(part, 50, 315, 270, 0, -50)
    if (part.centerY < 50):
        setValues(part, 75, 50, 0, 50, 0)

def onMousePress(x, y):
    # Move each part of the snake by the appropriate dx and dy. Then change
    # the part's values accordingly.
    ### (HINT: We have provided a function that you might find helpful!)
    ### Place Your Code Here ###
    for part in app.snake:
        part.centerX +=part.dx
        part.centerY +=part.dy
        changeValues(part)
    # Toggle app.bodyPartHeight property so that it alternates between 25 and 30.
    # Then, if the snake has fewer than 20 body parts, create a new one.
    ### (HINT: We have provided another function that you might find useful!)
    ### Place Your Code Here ###
    if(app.bodyPartHeight == 30):
        app.bodyPartHeight = 25
    else:
        app.bodyPartHeight = 30
    if len(app.snake) <20:
            createBodyPart(app.bodyPartHeight)
