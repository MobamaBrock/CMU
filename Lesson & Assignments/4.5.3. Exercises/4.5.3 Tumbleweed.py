import random

app.background = gradient('skyBlue', 'orange', start='top')
app.stepsPerSecond = 40

# background
Rect(0, 175, 400, 225,
     fill=gradient(rgb(235, 185, 40), rgb(255, 240, 0), start='top'))
Polygon(0, 175, 150, 175, 50, 100, fill=rgb(235, 185, 0))
Polygon(210, 175, 400, 175, 300, 100, fill=rgb(215, 155, 60))
Polygon(50, 175, 190, 175, 130, 120, fill=rgb(255, 235, 60))

# road
Polygon(0, 350, 0, 400, 400, 400, 400, 350, 210, 175, 190, 175, fill='grey')
Line(200, 175, 200, 400, fill=gradient('grey', 'silver', start='top'),
     lineWidth=10, dashes=True)

sandStorm = Group()
for i in range(10):
    sandStorm.add(
        Circle(random.randint(-300, 450), random.randint(25, 300), 1, fill='khaki')
        )

tumble = Group(Circle(200, 250, 20, fill='tan'))
tumble.dy = -5

def createTumbleweed():
    # A tumbleweed is drawn by creating a bunch of oval borders with varying
    # properties.
    for i in range(45):
        # Get a random position within 5 pixels of the point (200, 250) in
        # either direction.
        ### Place Your Code Here ###
        cx = randrange(195,205)
        cy = randrange(245,255)

        # Pick a random red and use that to find the green and blue.
        ### (HINT: The red should be between 180 and 215, inclusive.)
        ### (HINT: There's a simple relationship between the red and the blue
        #          and green. Use the Inspector to help figure out what it is!)
        ### Place Your Code Here ###
        red = randrange(180,215)
        green = red - 35
        blue = green - 35
        color = rgb(red,green,blue)

        # Gets a random height and uses that to get a width that makes the oval
        # more stretched out.
        width = random.randint(10, 85)
        if (width <= 30):
            height = random.randint(60, 85)
        else:
            height = random.randint(10, 60)

        angle = random.randint(0, 360)
        tumble.add(
            Oval(cx, cy, width, height, fill=None, border=color, dashes=(8, 3),
                 rotateAngle=angle)
            )

createTumbleweed()

def onStep():
    # Moves the tumbleweed.
    tumble.centerX += 8
    tumble.centerY += tumble.dy
    tumble.rotateAngle += 8
    tumble.dy += 0.4

    # Wraps the tumbleweed around.
    if (tumble.centerY >= 250):
        tumble.dy = -5
    if (tumble.left >= 400):
        tumble.right = 0

    # Moves the sand.
    for sand in sandStorm:
        sand.centerX += 40

        # When the sand moves off the screen, set its right to a random value
        # between -40 and 0, and set the centerY to a random position between
        # 0 and 300 (all inclusive).
        ### Place Your Code Here ###
        if sand.centerX > 400:
            sand.right = randrange(-40,0)
            sand.centerY = randrange(0,300)
