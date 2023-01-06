app.background = 'slateGray'

laserBarrier = Rect(125, 125, 150, 150, fill='slateGrey', border='red',
                    borderWidth=1)

# laser emitters
Circle(125, 125, 7)
Circle(275, 125, 7)
Circle(275, 275, 7)
Circle(125, 275, 7)

# glass shards
Polygon(170, 380, 170, 370, 180, 370, fill='snow', opacity=50)
Polygon(210, 385, 215, 370, 220, 375, fill='snow', opacity=50)
Polygon(180, 390, 185, 390, 190, 400, fill='snow', opacity=50)
Polygon(230, 385, 240, 385, 240, 390, fill='snow', opacity=50)
Polygon(160, 380, 170, 390, 165, 390, fill='snow', opacity=50)

# alarms
Rect(0, 0, 50, 50, fill='darkSlateGray')
alarm1 = Circle(25, 25, 10, fill='whiteSmoke')
alarm1Light = Circle(25, 25, 150, fill='crimson', opacity=20, visible=False)

Rect(350, 0, 50, 50, fill='darkSlateGray')
alarm2 = Circle(375, 25, 10, fill='whiteSmoke')
alarm2Light = Circle(375, 25, 150, fill='crimson', opacity=20, visible=False)

Rect(0, 350, 50, 50, fill='darkSlateGray')
alarm3 = Circle(25, 375, 10, fill='whiteSmoke')
alarm3Light = Circle(25, 375, 150, fill='crimson', opacity=20, visible=False)

Rect(350, 350, 50, 50, fill='darkSlateGray')
alarm4 = Circle(375, 375, 10, fill='whiteSmoke')
alarm4Light = Circle(375, 375, 150, fill='crimson', opacity=20, visible=False)

Rect(170, 170, 60, 60, fill='darkGray')
treasure = Polygon(180, 190, 185, 180, 215, 180, 220, 190, 200, 220,
                   fill=gradient('mediumSlateBlue', 'aqua', start='top'))
treasure.isHeld = False
Rect(175, 175, 50, 50, fill='snow', opacity=50)
def onMouseMove(x,y):
    # Only set off the alarms when the mouse is inside the laser barrier.
    ### Fix Your Code Here ###
    if laserBarrier.hits(x,y):
        alarm1.fill = 'crimson'
        alarm1Light.visible = True
        alarm2.fill = 'crimson'
        alarm2Light.visible = True
        alarm3.fill = 'crimson'
        alarm3Light.visible = True
        alarm4.fill = 'crimson'
        alarm4Light.visible = True
    # When we touch the treasure, pick it up.
    ### (HINT: We've defined a custom property for you above!)
    ### Place Your Code Here ###
    if treasure.hits(x,y):
        treasure.isHeld = True
    # If we have taken the treasure, move it with the mouse.
    ### Place Your Code Here ####
 if treasure.isHeld:
        treasure.centerX = x
        treasure.centerY = y
