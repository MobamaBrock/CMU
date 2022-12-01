app.background = gradient('lightSkyBlue', 'deepSkyBlue', start='top')

# koala
Oval(200, 425, 220, 360, fill=gradient('darkGrey', 'grey', start='top'))
Oval(200, 425, 160, 280, fill='lightGrey')
Circle(130, 150, 40, fill=gradient('grey', 'silver', start='right-bottom'))
Circle(130, 150, 25, fill='lightGrey')
Circle(270, 150, 40, fill=gradient('grey', 'silver', start='right-bottom'))
Circle(270, 150, 25, fill='lightGrey')
Circle(200, 200, 80, fill=gradient('silver', 'grey', start='top'))
Oval(200, 210, 20, 40)
mouth = Line(185, 240, 215, 240)

# koala's eyes
Oval(180, 180, 10, 20)
Oval(220, 180, 10, 20)
pupils = Group(
    Oval(180, 185, 3, 6, fill='white'),
    Oval(220, 185, 3, 6, fill='white')
    )

# leaf
Oval(170, 260, 25, 45, fill=gradient('seaGreen', 'green', start='bottom'),
     rotateAngle=55)
Line(197, 240, 155, 270, fill='darkGreen')

# bald spot
Oval(200, 138, 50, 28, fill=gradient('moccasin', 'gainsboro'))

noHat = Group()
bowlerHat = Group(
    Oval(200, 145, 180, 40),
    Oval(200, 115, 80, 100),
    Arc(200, 125, 80, 20, 90, 180, border='white', borderWidth=10),
    )
sombrero = Group(
    Arc(200, 130, 270, 50, 70, 220, fill='orange', border='red', borderWidth=3),
    Arc(200, 130, 270, 50, 70, 220, fill=None, border='green', borderWidth=3,
        dashes=(20, 20)),
    Oval(200, 90, 80, 100, fill='gold'),
    Rect(160, 90, 80, 50, fill=gradient('gold', 'orange', start='top'))
    )
wizardHat = Group(
    # left hat
    Oval(125, 115, 80, 15, fill='midnightBlue'),
    Polygon(105, 112, 125, 32, 145, 112, fill='blue'),
    Star(125, 90, 10, 5, fill='white'),

    # right hat
    Oval(275, 115, 80, 15, fill='midnightBlue'),
    Polygon(255, 112, 275, 32, 295, 112, fill='blue'),
    Oval(275, 110, 36, 5, fill='blue'),
    Star(275, 90, 10, 5, fill='white'),

    # center hat
    Oval(200, 150, 200, 30, fill='midnightBlue'),
    Polygon(150, 150, 200, -5, 250, 150, fill='blue'),
    Star(225, 125, 10, 5, fill='white'),
    Star(200, 85, 10, 5, fill='white'),
    Star(175, 125, 10, 5, fill='white'),
    Star(200, 40, 10, 5, fill='white')
    )

sombrero.visible = False
bowlerHat.visible = False
wizardHat.visible = False

# Each element of app.hats is a group that draws a hat.
app.hats = [ noHat, bowlerHat, sombrero, wizardHat ]
app.index = 0

def adjustSmile():
    currentHat = app.hats[app.index]

    # If no hat is on, the koala frowns. Otherwise it smiles.
    if (currentHat == noHat):
        pupils.centerY = 185
        mouth.rotateAngle = 0
    else:
        pupils.centerY = 175
        mouth.rotateAngle = 12

def onMousePress(mouseX, mouseY):
    if app.index == 3:
        app.hats[app.index].visible = False
        app.index = 0
        adjustSmile()
    else:
        app.hats[app.index].visible = False
        app.index += 1
        app.hats[app.index].visible = True
        adjustSmile()
