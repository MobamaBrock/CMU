def drawFace(x, y, backgroundColor):
    Rect(x - 100, y - 100, 200, 200, fill=backgroundColor)
    Circle(x - 25, y - 20, 20, fill='white')
    Circle(x - 25, y - 20, 7)
    Circle(x + 25, y - 20, 20, fill='white')
    Circle(x + 25, y - 20, 7)

drawFace(100, 100, 'salmon')
drawFace(300, 100, 'paleTurquoise')
drawFace(100, 300, 'paleGreen')
drawFace(300, 300, 'plum')

redMouth = Label('-', 100, 120, size=50)
blueMouth = Label('-', 300, 120, size=50)
greenMouth = Label('-', 100, 320, size=50)
purpleMouth = Label('-', 300, 320, size=50)

def onMousePress(x, y):
    # Based on the face you click, switch the mouth to either - or o.
    ### (HINT: First figure out which face you clicked on, then check
    #          whether that face's mouth should switch to - or to o.)
    ### Place Your Code Here ###
    if x <= 200:
        if y <= 200:
            if redMouth.value == '-':
                redMouth.value = 'o'
            else:
                redMouth.value = '-'
        else:
            if greenMouth.value == '-':
                greenMouth.value = 'o'
            else:
                greenMouth.value = '-'
    else:
        if y <= 200:
            if blueMouth.value == '-':
                blueMouth.value = 'o'
            else:
                blueMouth.value = '-'
        else:
            if purpleMouth.value == '-':
                purpleMouth.value = 'o'
            else:
                purpleMouth.value = '-'
