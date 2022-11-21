app.background = 'lightSteelBlue'
# custom app property
app.isSnowing = False
# These two lines drawn all the raindrops!
rain = Line(200, 0, 200, 300, fill='steelBlue', lineWidth=325, dashes=(8, 16))
Line(0, 150, 400, 150, fill='lightSteelBlue', lineWidth=300, dashes=(50, 8))
# plant
stem = Line(200, 200, 200, 300, fill='darkGreen', lineWidth=10)
leaf1 = Oval(180, 180, 30, 60, fill='darkGreen', rotateAngle=-45)
leaf2 = Oval(220, 180, 30, 60, fill='darkGreen', rotateAngle=45)
ground = Rect(0, 300, 400, 100, fill='darkGreen')
def onMousePress(mouseX, mouseY):
    # Change the season.
    ### (HINT: We defined a custom app property above that might be helpful!)
    ### Place Your Code Here ###
    pass
    # This resets the ground and the plant.
    ground.top = 300
    ground.height = 100
    stem.y1 = 200
    leaf1.centerY = 180
    leaf2.centerY = 180
    if app.isSnowing == False:
        app.isSnowing=True
        ground.fill='white'
        rain.fill='white'
    else:
        app.isSnowing=False
        ground.fill='darkGreen'
        rain.fill='steelBlue'
def onMouseMove(mouseX, mouseY):
    # When it is snowing, the snow builds up. Otherwise, the plant grows.
    if (app.isSnowing == True):
        ground.top -= 2
        ground.height += 2
    else:
        stem.y1 -= 2
        leaf1.centerY -= 2
        leaf2.centerY -= 2
