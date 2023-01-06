# scenery
Rect(0, 0, 400, 150, fill='lightBlue')
Rect(0, 150, 400, 95, fill='oliveDrab')
Polygon(170, 150, 230, 150, 380, 245, 20, 245, fill='tan')
Circle(85, 55, 20, fill='white', opacity=70)
Circle(66, 60, 15, fill='white', opacity=70)
Circle(105, 60, 15, fill='white', opacity=70)
Circle(290, 55, 20, fill='white', opacity=70)
Circle(270, 60, 13, fill='white', opacity=70)
Circle(310, 60, 15, fill='white', opacity=70)
Circle(325, 65, 10, fill='white', opacity=70)
# dashboard
Oval(200, 250, 300, 100, fill='lightSlateGray')
Polygon(0, 245, 30, 245, 70, 225, 330, 225, 370, 245, 400, 245, 400, 400,
        0, 400, fill='lightSlateGray')
Oval(200, 270, 300, 100)
Rect(50, 270, 300, 50)
s = Circle(200, 370, 160, fill=None, border=rgb(85, 95, 110),
                       borderWidth=45)
Polygon(80, 380, 80, 350, 140, 340, 260, 340, 320, 350, 320, 380,
        260, 385, 245, 400, 155, 400, 140, 385, fill=rgb(85, 95, 110))
# steering wheel grips
rg=Polygon(38, 355, 43, 330, 90, 345, 88, 360, 88, 380, 90, 395, 43, 410, 38, 385,
        fill=rgb(65, 73, 84))
lg=Polygon(362, 355, 357, 330, 310, 345, 312, 360, 312, 380, 310, 395, 357, 410,
        362, 385, fill=rgb(65, 73, 84))
l = Circle(62, 370, 21, fill='saddleBrown')
r = Circle(337, 370, 21, fill='saddleBrown')
m = Label('Good!', 200, 180, fill='white', size=15, bold=True)
def onMousePress(x, y):
    # Move the hands to where the mouse is.
    ### Place Your Code Here ###
    # Update the message. There are 3 possible messages:
    #   if the left hand is fully on the steering wheel,
    #   if the left hand is touching the wheel, or
    #   if the left hand is not touching the wheel.
    ### Place Your Code Here ###
        l.centerY= y
    r.centerY= y
    if l.centerY>352:
        m.value= 'Good!'
    elif l.hitsShape(s):
        m.value= 'Close!'
    else:
        m.value='Put your hands on the steering wheel!'
