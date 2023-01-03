app.background = gradient('midnightBlue', 'royalBlue', start='top')

Rect(50, 10, 300, 380, fill=gradient('whiteSmoke', 'white', start='top'))
e = Line(200, 20, 200, 30, lineWidth=250, dashes=True)
app.index = 0
pageNumber = Label(1, 335, 375, size=20)

def onKeyPress(key):
    # On any key press, the essay should get longer.
    # If you reach the end of the page, go to a new page.
    ### (HINT: To go to a new page, modify essay to the shortest value
    #          and increase the pageNumber.)
    ### Place Your Code Here ###

    if app.index < 35:
        e.y2 += 10
        app.index +=1
    else:
        e.y2 = 30
        app.index = 0
        pageNumber.value += 1
