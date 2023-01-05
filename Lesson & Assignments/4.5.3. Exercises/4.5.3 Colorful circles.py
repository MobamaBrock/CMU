import random
app.index = 0
app.background = 'darkBlue'
app.stepsPerSecond = 3

circles = Group()

def onStep():
    colors = [ 'lightCoral', 'deepSkyBlue', 'mediumPurple',
               'lavender', 'crimson' ]

    # Loop through the colors and add a circle for each color.
    ### Place Your Code Here ###

    # Each circle should have a random x and y coordinate between 0 and
    # 400 and a random radius between 5 and 20. (all inclusive.)
    ### Place Your Code Here ###
    for i in range(5):
        circles.add(Circle(random.randint(0,400),random.randint(0,400),random.randint(5,20),fill=colors[app.index],border = 'black',borderWidth = 3))
        app.index += 1
        app.index = app.index % 5
    # Increases the size of all the circles until they get to 50, then
    # removes them.
    for circle in circles.children:
        circle.radius += 5
        if (circle.radius > 50):
            circles.remove(circle)
