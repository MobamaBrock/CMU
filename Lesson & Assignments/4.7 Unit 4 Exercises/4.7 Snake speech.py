 app.background = 'peru'

# snake
Oval(130, 350, 500, 350, fill=None, border='lightGreen', borderWidth=45)
Oval(25, 200, 400, 200, fill='peru')
Polygon(80, 205, 85, 210, 80, 215, 130, 215, 130, 205, fill='crimson')
Oval(185, 210, 120, 90, fill='lightGreen')
Circle(160, 190, 5)
Circle(160, 230, 5)

# speech bubble
Polygon(70, 110, 120, 110, 130, 160, fill='white')
Oval(200, 70, 400, 120, fill='white')

snakeText = Label('', 200, 70, size=20)

def makeSnakeSpeech():
    # Transforms the inputted text into snake speech.
    text = app.getTextInput('What should the snake say?')
    textlist = []
    for i in range(len(text)):
        if text[i] == 's':
            textlist.insert(i,'sssss')
            print("hi")
        else:
            textlist.insert(i,text[i])
    snakeText.value = ''
    for i in range(len(textlist)):
        snakeText.value = snakeText.value + textlist[i]
    
    # Create a new string that is the same as the string the user inputs, but
    # with every 's' replaced with 'sssss'.
    ### Place Your Code Here ###

def onMousePress(mouseX, mouseY):
    makeSnakeSpeech()
