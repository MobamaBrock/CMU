app.background = 'dimGray'
Line(200, 0, 200, 400, fill='linen', lineWidth=400, opacity=50, dashes=(3, 15))
# frozen yogurt machine
Rect(50, 50, 300, 300, fill='silver')
Rect(60, 60, 85, 50, fill=gradient('lightSkyBlue', 'white', start='top'))
Rect(155, 60, 90, 50, fill=gradient('pink', 'peachpuff', start='top'))
Rect(255, 60, 85, 50, fill=gradient('peru', 'wheat', start='top'))
Rect(140, 140, 120, 40)
Rect(60, 190, 280, 150, fill='darkGray')
Rect(60, 330, 280, 10, fill='white')
# handles
handle1 = Line(170, 120, 170, 165, fill='white', lineWidth=16)
handle2 = Line(200, 120, 200, 165, fill='white', lineWidth=16)
handle3 = Line(230, 120, 230, 165, fill='white', lineWidth=16)
Circle(170, 165, 8, fill='white')
Circle(200, 165, 8, fill='white')
Circle(230, 165, 8, fill='white')
# frozen yogurt
flow1 = Line(170, 190, 170, 250, lineWidth=10, visible=False,
             fill=gradient('lightSkyBlue', 'white', start='left'))
flow2 = Line(200, 190, 200, 250, lineWidth=10, visible=False,
             fill=gradient('pink', 'peachpuff', start='left'))
flow3 = Line(230, 190, 230, 250, lineWidth=10, visible=False,
             fill=gradient('peru', 'wheat', start='left'))
cup = Polygon(180, 300, 220, 300, 215, 330, 185, 330, fill='crimson')
def pressHandle(handle, flow):
    handle.visible = False
    flow.visible = True
    cup.centerX = flow.centerX
    cup.top = flow.bottom
def onMousePress(x, y):
    # Reposition the cup to catch the yogurt flow if a handle is pressed!
    ### (HINT: Use a helper function we defined above. What arguments should
    #          you pass into the function?)
    ### Place Your Code Here ###
    if handle1.hits (x,y):
        handle1.visible = False
        flow1.visible = True
        cup.centerX = 170
        cup.top = 250
    if handle2.hits (x,y):
        handle2.visible = False
        flow2.visible = True
        cup.centerX = 200
        cup.top = 250
    if handle3.hits (x,y):
        handle3.visible = False
        flow3.visible = True
        cup.centerX = 230
        cup.top = 250
def onMouseRelease(x, y):
    # This resets the machine and the cup.
    handle1.visible = True
    handle2.visible = True
    handle3.visible = True
    flow1.visible = False
    flow2.visible = False
    flow3.visible = False
    cup.centerX = 200
    cup.bottom = 330
