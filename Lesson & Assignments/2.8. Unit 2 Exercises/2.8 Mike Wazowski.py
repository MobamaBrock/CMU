app.background = 'limeGreen'
# mouth
Oval(200, 340, 120, 40)
Oval(200, 345, 130, 40, fill='limeGreen')
eye = Circle(200, 180, 100, fill='white', border='chartreuse', borderWidth=10)
Circle(200, 180, 40, fill='black', border='lightSeaGreen', borderWidth=20)
eyelid = Circle(200, 180, 100, fill='chartreuse', visible=False)
finger = Circle(-50, 200, 20, fill='tan')
# When the finger is poking the eye, close the eyelid.
def onMousePress(x, y):
    finger.centerX = x
    finger.centerY = y
    if finger.hitsShape(eyelid)==True:
        eyelid.visible=True
    else:
        eyelid.visible=False
