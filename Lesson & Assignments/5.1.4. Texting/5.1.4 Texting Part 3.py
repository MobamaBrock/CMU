import random

app.stepsPerSecond = 1

# word choices
app.myVerbs = ['like', 'love', 'adore', 'dislike', 'hate', 'loathe']
app.myAnimals = ['dogs', 'cats', 'fish', 'birds', 'snakes', 'rabbits']
app.theirResponses = ['What?!', 'Me too!', 'No way...', 'Same! :)', 'Interesting.']

border = Rect(0, 0, 400, 400, fill=None, border='grey', borderWidth=30)

# text box
Rect(30, 330, 340, 40, fill='gainsboro')
Circle(55, 350, 15, fill='white')
Circle(290, 350, 15, fill='white')
Line(55, 350, 290, 350, fill='white', lineWidth=30)
Label('Message', 80, 350, fill='gainsboro')
Label('Send', 335, 350)

texts = Group()
texts.amITexting = True

def drawMessage(message, isFromMyself):
    textBubble = Group(
        Circle(15, 305, 15),
        Circle(100, 305, 15),
        Line(15, 305, 100, 305, lineWidth=30)
        )


    # This function now takes a message and a boolean isFromMyself. Depending on
    # if this text is from me or not, recolor and reposition the bubble. Then add
    # a polygon for the bubble's tail and the text bubble message.
    if isFromMyself == True:
        textBubble.fill = 'dodgerBlue'
        textBubble.right = 350
        textBubble.add(Polygon(335,320,360, 320,335,305 , fill = 'dodgerBlue'))
        textBubble.add(Label(message,293,textBubble.centerY, fill = 'white'))
    else:
        textBubble.fill = 'gainsboro'
        textBubble.left= 50
        textBubble.add(Polygon(65,320,40, 320,65,305 , fill = 'gainsboro'))
        textBubble.add(Label(message,108,textBubble.centerY))

    texts.add(textBubble)

def moveTexts():
    for i in texts:
        i.centerY -=40
        if i.centerY < 30:
            texts.remove(i)
    # Move each text message up to make space for the new one.
    # Remove the text message if it leaves the texting space.
    pass


def onStep():
    moveTexts()
    # If it is my turn to text, get a random verb and a random animal. Then create
    # a sentence using the form "I [verb] [animal].". Draw that message.
    # If it isn't my turn to text, get and draw a random response.
    ### (HINT: We have defined several lists as app custom properties, and
    #          a texts custom property above.)
    ### Place Your Code Here ###
    if texts.amITexting == True:
        texts.amITexting = False
        message = 'I '+ random.choice(app.myVerbs) +' '+ random.choice(app.myAnimals) + '.'
        drawMessage(message, True)
    elif texts.amITexting == False:
        texts.amITexting = True
        message = random.choice(app.theirResponses)
        drawMessage(message, False)
