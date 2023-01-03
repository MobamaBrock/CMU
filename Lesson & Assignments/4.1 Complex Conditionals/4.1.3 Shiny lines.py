app.background = 'black'

Line(200, 0, 200, 400, fill='white')
Line(0, 200, 400, 200, fill='white')

def onMouseMove(x,y):
    # Depending on the quadrant the mouse is on, draw a gradient line from
    # the closest corner.
    ### (HINT: Check x and y location separately to determine quadrant.)
    ### Place Your Code Here ###
    if x <= 200:
        if y <= 200:
            Line(0,0,x,y,fill=gradient('red','black'))
        else:
            Line(0,400,x,y,fill=gradient('blue','black'))
    else:
        if y <= 200:
            Line(400,0,x,y,fill=gradient('green','black'))
        else:
            Line(400,400,x,y,fill=gradient('yellow','black'))
