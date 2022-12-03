app.background = rgb(55, 225, 205)
app.stepsPerSecond = 25

# body
outerHead = Oval(200, 300, 210, 220, fill=rgb(250, 200, 230))
animal = Oval(200, 300,  180, 200, fill=rgb(250, 220, 240))
animal.type = 'jellyfish'
Rect(95, 300, 210, 100, fill=rgb(55, 225, 205))

# tentacles
tentacles = Line(120, 340, 280, 340, fill=rgb(250, 220, 240), lineWidth=80,
                 dashes=(20, 15))

# eyes
Circle(155, 265, 10)
Circle(245, 265, 10)
Circle(155, 260, 5, fill='grey')
Circle(245, 260, 5, fill='grey')

# mouth
Circle(200, 265, 15, fill=rgb(250, 120, 180))
mouthCover = Rect(185, 250, 30, 15, fill=rgb(250, 220, 240))

# bubbles
Circle(120, 30, 40, fill=gradient('lightCyan', 'lavender'), opacity=20,
       border=gradient('powderBlue', 'cornflowerBlue', start='top'))
Circle(120, 90, 30, fill=gradient('lightCyan', 'lavender'), opacity=40,
       border=gradient('powderBlue', 'cornflowerBlue', start='top'))
Circle(120, 150, 20, fill=gradient('lightCyan', 'lavender'), opacity=60,
       border=gradient('powderBlue', 'cornflowerBlue', start='top'))
Circle(120, 210, 10, fill=gradient('lightCyan', 'lavender'), opacity=80,
       border=gradient('powderBlue', 'cornflowerBlue', start='top'))
Circle(120, 270, 1, fill=gradient('lightCyan', 'lavender'),
       border=gradient('powderBlue', 'cornflowerBlue', start='top'))

ink = Polygon(180, 300, 170, 335, 145, 375, 110, 400, 290, 400, 255, 375,
              230, 335, 220, 300, opacity=85, visible=False)
animal.type = 'squid'
def onMousePress(mouseX, mouseY):
    # Define these local variables depending on what animal is showing.
    ### (HINT: Use the custom property animal.type, and change the type
    #          each time you press the mouse!)
    ### Fix Your Code Here ###
    if animal.type == 'jellyfish':
        outerHead.fill = rgb(250, 200, 230)
        outerHead.height = 200 + 20
        animal.fill = rgb(250, 220, 240)
        animal.height = 200
        mouthCover.fill = rgb(250, 220, 240)
        tentacles.fill = rgb(250, 220, 240)
        animal.type = 'squid'
        print(animal.type)
        ink.visible = False
    else:
        print(True)
        ink.visible = True
        tentacles.toFront()
        outerHead.fill = 'black'
        outerHead.height = 400
        animal.fill = 'dimGrey'
        animal.height = 380
        mouthCover.fill = 'dimGrey'
        tentacles.fill = 'dimGrey'
        animal.type = 'jellyfish'
        print(animal.type)
