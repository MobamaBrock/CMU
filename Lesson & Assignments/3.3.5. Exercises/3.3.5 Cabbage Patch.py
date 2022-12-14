app.background = gradient('sienna', 'chocolate')

def drawCabbage(x, y):
    cabbage = Group(
        Star(200, 200, 50, 8, fill='mediumSeaGreen', rotateAngle=30, roundness=80),
        Star(200, 200, 40, 8, fill='lightGreen', rotateAngle=50, roundness=80),
        Star(200, 200, 30, 8, fill='paleGreen', rotateAngle=70, roundness=80)
        )
    cabbage.centerX = x
    cabbage.centerY = y

def drawCabbages():
    for x in range(5):
        for y in range(5):
            drawCabbage(100*y,100*x)
