app.stepsPerSecond = 5

app.reds = [ 255, 220, 200, 150, 125, 100, 90, 75, 50, 10 ]
app.y = 0

Rect(0, 0, 400, 400)

def drawRowOfRectangles():
    x = 0
    # Draws a rectangle for each red value.
    for red in app.reds:
        Rect(x, app.y, 40, 25, fill=rgb(red, 0, 0))
        x += 40

def onMousePress(mouseX, mouseY):
    drawRowOfRectangles()

    # Remove the last value from the app.reds list and store it in newVal.
    ### Fix Your Code Here ###
    app.reds.insert(0,app.reds.pop())

    # Creates a new list with the last value.


    # Add all of the other red values to the newList.
    ### (HINT: Loop over app.reds and add each element to newList.)
    ### Place Your Code Here ###

    # Sets app.reds equal to the new list.
  

    # Shifts where the next rectangle will be drawn.
    app.y += 25
