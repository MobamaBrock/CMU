import random

app.stepsPerSecond = 1

border = Rect(0, 0, 400, 400, fill=None, border='grey', borderWidth=30)

# text box
Rect(30, 330, 340, 40, fill='gainsboro')
Circle(55, 350, 15, fill='white')
Circle(290, 350, 15, fill='white')
Line(55, 350, 290, 350, fill='white', lineWidth=30)
Label('Message', 80, 350, fill='gainsboro')
Label('Send', 335, 350)

texts = Group()

def drawMessage():
    textBubble = Group(
        Circle(55, 305, 15),
        Circle(140, 305, 15),
        Line(55, 305, 140, 305, lineWidth=30)
        )
    textBubble.fill = 'gainsboro'
    textBubble.centerX = random.choice([ 100, 300 ])
    texts.add(textBubble)

def moveTexts():
    #### START OF BLOCK MOVE_TEXTS ####
    for i in texts:
        i.centerY -=40
        if i.centerY < 30:
            texts.remove(i)
    # Move each text message up to make space for the new one.
    # Remove the text message if it leaves the texting space.
    ### Place Your Code Here ###
    pass

    #### END OF BLOCK ####

def onStep():
    moveTexts()
    drawMessage()
