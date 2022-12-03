app.background = 'burlyWood'

# Stores all pieces of sushi on the conveyor belt.
app.sushiOrder = [ ]

# conveyor belt
Rect(0, 80, 400, 100, fill=rgb(240, 240, 240))
Line(0, 130, 400, 130, fill='gainsboro', lineWidth=100, dashes=(2, 30))

# table decor
Rect(40, 20, 60, 40, fill=rgb(60, 60, 60), border='brown', borderWidth=4)
Rect(50, 30, 40, 20, fill=rgb(50, 30, 10))
Rect(120, 20, 40, 40, fill=rgb(60, 60, 60), border='brown', borderWidth=4)
Rect(156, 20, 40, 40, fill=rgb(60, 60, 60), border='brown', borderWidth=4)
Circle(140, 40, 10, fill='yellowGreen')
Circle(176, 40, 10, fill='pink')
Rect(220, 30, 160, 5, fill='navajoWhite')
Rect(220, 45, 160, 5, fill='navajoWhite')

def makeSushi(color):
    # Draws a piece of sushi at the left of the conveyor belt using the color given.
    piece = Group (
        Rect(50, 110, 25, 50, fill='white', border='gainsboro'),
        Rect(50, 100, 25, 50, fill=color),
        Line(50, 100, 75, 150, fill=rgb(240, 240, 240),
             lineWidth=45, dashes=(2, 6)),
        Rect(50, 100, 25, 50, fill=None, border=color)
        )
    piece.centerX = 12
    # Add the new sushi to the front of the order.
    ### Place Your Code Here ###
    app.sushiOrder.insert(0,piece)
def moveConveyorBelt():
    # When the conveyor belt moves, each piece of sushi moves to the right.
    for piece in app.sushiOrder:
        piece.centerX += 50
def eat():
    app.sushiOrder.pop().visible = False
# ordering buttons on menu
salmon = Group(
    Rect(40, 225, 100, 175, fill='cornSilk'),
    Circle(110, 320, 20, fill='coral', border='sienna'),
    Label('Salmon', 110, 365, fill=rgb(85, 30, 5))
    )
tuna = Group(
    Rect(140, 225, 120, 175, fill='cornSilk'),
    Circle(200, 320, 20, fill='crimson', border='sienna'),
    Label('Tuna', 200, 365, fill=rgb(85, 30, 5))
    )
yellowTail = Group(
    Rect(260, 225, 100, 175, fill='cornSilk'),
    Circle(290, 320, 20, fill='lightCoral', border='sienna'),
    Label('Yellow Tail', 290, 365, fill=rgb(85, 30, 5))
    )

# menu details
Rect(40, 225, 320, 180, fill=None, border='sienna')
Label('Sushi menu', 60, 250, size=16, fill=rgb(85, 30, 5), align='left')
Line(57, 263, 147, 263, fill='sienna')

def onMousePress(mouseX, mouseY):
    # When the menu is pressed, the conveyor belt should move previously ordered
    # sushi to the right and a properly colored sushi should be added to the
    # left of the conveyor belt.
    if salmon.hits(mouseX,mouseY):
        makeSushi('coral')
        moveConveyorBelt()
    elif tuna.hits(mouseX,mouseY):
        makeSushi('crimson')
        moveConveyorBelt()
    elif yellowTail.hits(mouseX,mouseY):
        makeSushi('lightCoral')
        moveConveyorBelt()
    else:
        if len(app.sushiOrder) > 0:
            eat()
    # Otherwise, you should eat the sushi from right to left.
    ### (HINT: Be sure to set its visibility to False!)
    ### Place Your Code Here ###
    pass
