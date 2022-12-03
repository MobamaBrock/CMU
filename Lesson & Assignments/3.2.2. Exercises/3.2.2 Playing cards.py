app.background = gradient('mediumSeaGreen', 'seaGreen')

# variables representing the card's suit
app.diamonds = 0
app.hearts = 1
app.clubs = 2
app.spades = 3

# variables for the red suit color and black suit color
app.redColor = 'tomato'
app.blackColor = 'dimGrey'

def drawHearts(x, y, color):
    # draws a heart
    Polygon(x - 22, y - 10, x - 2, y - 10, x - 12, y - 20, fill=color)
    Polygon(x + 22, y - 10, x + 2, y - 10, x + 12, y - 20, fill=color)
    Polygon(x - 22, y - 5, x + 22, y - 5, x, y + 20, fill=color)

def drawDiamonds(x, y, color):
    # draws a diamond
    Rect(x, y, 30, 30, fill=color, rotateAngle=45, align='center')

def drawClubs(x, y, color):
    # draws a clover (clubs)
    Rect(x, y - 10, 12, 12, fill=color, rotateAngle=45, align='center')
    Rect(x - 12, y + 5, 12, 12, fill=color, rotateAngle=45, align='center')
    Rect(x + 12, y + 5, 12, 12, fill=color, rotateAngle=45, align='center')

def drawSpades(x, y, color):
    # draws a spade
    Polygon(x, y - 20, x - 20, y + 10, x + 20, y + 10, fill=color)
    Polygon(x, y + 12, x - 8, y + 20, x + 8, y + 20, fill=color)

def drawCard(x, y, rank, suit):
    # draws the base of the card and its shadow

    Rect(x - 10, y, 100, 150, opacity=10)
    Rect(x, y, 100, 150, fill='white', border='darkGrey')
    
    # Depending on the card's suit, set the helper variable, suitColor, accordingly.
    # Then draw the correct symbol for the suit at the middle of the card.
    ### (HINT: Hearts and diamonds are red cards, clubs and spades are black cards.)
    ### (HINT: There are some helpful functions written for you above.)
    ### Fix Your Code Here ###

    if suit == app.diamonds:
        drawDiamonds(x +50,y+75,'tomato')
        print('yes')
    if suit == app.hearts:
        drawHearts(x +50,y+75,'tomato')
        print('yes')
    if suit == app.clubs:
        drawClubs(x +50,y+75,'dimGrey')
        print('yes')
    if suit == app.spades:
        drawSpades(x +50,y+75,'dimGrey')
        print('yes')
        
    # draws the card using the determined suit color
    if suit == app.diamonds:
        suitColor = app.redColor
    if suit == app.hearts:
        suitColor = app.redColor
    if suit == app.clubs:
        suitColor = app.blackColor
    if suit == app.spades:
        suitColor = app.blackColor
        
    Rect(x + 5, y + 5, 90, 140, fill=None, border=suitColor, dashes=True)
    Polygon(x, y, x + 15, y, x, y + 15, fill=suitColor)
    Polygon(x + 100, y, x + 85, y, x + 100, y + 15, fill=suitColor)
    Polygon(x, y + 150, x + 15, y + 150, x, y + 135, fill=suitColor)
    Polygon(x + 100, y + 150, x + 85, y + 150, x + 100, y + 135, fill=suitColor)
    Label(rank, x + 20, y + 20, fill=suitColor)
    Label(rank, x + 80, y + 130, fill=suitColor)
