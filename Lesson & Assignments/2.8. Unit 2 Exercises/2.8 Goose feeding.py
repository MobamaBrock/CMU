app.background = gradient('lightSalmon', 'lightCoral', 'mediumOrchid',
                          start='bottom')
# custom app property
app.foodCounter = 0
# grass and pond
Rect(250, 200, 150, 200, fill='oliveDrab')
Rect(0, 220, 250, 180, fill='steelBlue')
# clouds
Circle(100, 50, 30, fill='white', opacity=90)
Circle(120, 60, 20, fill='white', opacity=90)
Circle(80, 55, 25, fill='white', opacity=90)
Circle(300, 50, 30, fill='white', opacity=90)
Circle(320, 55, 25, fill='white', opacity=90)
Circle(280, 60, 20, fill='white', opacity=90)
Circle(340, 60, 20, fill='white', opacity=90)
# goose
goose = Polygon(40, 255, 90, 255, 85, 235, 92, 225, 100, 225, 115, 230,
                115, 235, 100, 245, 110, 260, 95, 285, 55, 285,
                fill='white', visible=False)
gooseBeak = Polygon(115, 230, 115, 235, 125, 234, 125, 232, fill='orange',
                    visible=False)
goose.speed = 15
def m():
    goose.visible = True
    gooseBeak.visible = True
def mg():
    goose.centerX += goose.speed
    gooseBeak.centerX += goose.speed
def onMousePress(mouseX, mouseY):
    # This draws a piece of food.
    Circle(mouseX, mouseY, 5, fill='wheat')
    app.foodCounter=app.foodCounter + 1
    print (app.foodCounter)
    # Update the food count.
    ### (HINT: We've defined an app custom property above for you.)
    ### Place Your Code Here ###
    # Make the goose appear if there is enough food. If there are at least 5
    # pieces of food, the goose should get closer to the land. Once the goose
    # is near the land, it shouldn't get any closer.
    ### (HINT: We've defined 2 functions above, and another custom property
    #          that might be helpful!)
    ### (HINT: When the goose stops, its speed is 0.)
    ### Place Your Code Here ###
        if app.foodCounter == 2:
        m()
   
    if app.foodCounter == 5 or app.foodCounter>5:
        mg()
    
    if app.foodCounter == 11:
        goose.speed = 0
