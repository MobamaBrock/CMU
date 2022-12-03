app.background = 'skyBlue'
app.lightColor = 'lightCoral'
app.darkColor = 'darkRed'
app.colorCycle = 0

roseBush = Group(
    Oval(220, 130, 150, 120, fill='seaGreen'),
    Oval(130, 180, 210, 150, fill='seaGreen'),
    Oval(20, 240, 180, 150, fill='seaGreen'),
    Oval(320, 180, 210, 170, fill='seaGreen'),
    Rect(0, 200, 400, 200, fill='seaGreen')
    )

def getRoseColors():
    # Picks the next color for the rose to be.
    if (app.colorCycle == 0):
        app.lightColor = 'lightCoral'
        app.darkColor = 'darkRed'
    elif (app.colorCycle == 1):
        app.lightColor = 'mistyRose'
        app.darkColor = 'pink'
    else:
        app.lightColor = 'gold'
        app.darkColor = 'orange'

    app.colorCycle += 1
    app.colorCycle = app.colorCycle % 3

def drawPetalRing(numberOfPetals, x, y):
    
    width = 1.5 * numberOfPetals
    height = 3 * numberOfPetals
    
    # Create a ring of petals.
    for i in range(numberOfPetals):
        angle = 30 * i
        if i % 2 ==0:
            color = app.lightColor
        else:
            color = app.darkColor
        

        # Alternate whether the color of the petal is light or dark.
        ### (HINT: The first petal should be the light color.)
        ### Place Your Code Here ###

        # Draw a rectangular petal using the defined variables.
        ### Place Your Code Here ###
        Rect(x,y,width,height,fill = color, rotateAngle = angle, align = 'center')
def onMousePress(mouseX, mouseY):
    numberOfPetalsInRing = [ 19, 17, 13, 11, 7, 5, 1 ]
    # If you click on the roseBush, draw a rose.
    if (roseBush.hits(mouseX, mouseY) == True):
        getRoseColors()
        for x in range(len(numberOfPetalsInRing)):
            drawPetalRing(numberOfPetalsInRing[x], mouseX, mouseY)    
    

        # To draw a rose, draw one petal ring for each number in the
        # numberOfPetalsInRing list.
        ### Fix Your Code Here ###
