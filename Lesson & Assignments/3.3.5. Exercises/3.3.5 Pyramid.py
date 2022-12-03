app.background = gradient(rgb(25, 25, 180), rgb(25, 25, 80), start='right-top')

Star(350, 50, 53, 500, fill='maroon')
Star(350, 50, 28, 500, roundness=90)
Rect(0, 365, 400, 135, fill='seaGreen')

pyramid = Group()
def drawPyramid(blockHeight):
    # Draw the layers leading up to the top of the pyramid.
    ### (HINT: Using an align of 'bottom' will make it easier!)
    ### Place your code here ###
# 260,140,320,80    
    stairsTop = 380-blockHeight*6
    # This variable defines the top of where the stairs should end.
    startx = 130
    starty = 380 - blockHeight*8
    width = 140
    for i in range(8):
        Rect(startx,starty,width,blockHeight,fill=gradient('saddleBrown','darkGoldenRod',start='top'),border='black',borderWidth=1)
        startx -= 15
        width += 30
        starty += blockHeight
    
    
    # Polygon for the staircase
    
    Polygon(85, 380, 160, stairsTop, 240, stairsTop, 315, 380,
            fill=gradient('sienna', 'goldenrod', start='top'), border='black')

    # Chamber at the top of the pyramid
    Rect(200, stairsTop, 40, 15, align='bottom'),
    Rect(200, 380-blockHeight*7, 180, 5, fill='darkGoldenrod', border='black', align='bottom')
    Rect(200, 380-blockHeight*7, 180, 5, fill='darkGoldenrod',border='black', align='top')
    
    # mist
    mist = Group(
        Star(150, 345, 50, 600, opacity=40, fill='white'),
        Star(175, 351, 48, 600, opacity=30, fill='white'),
        Star(200, 350, 52, 600, opacity=30, fill='white'),
        Star(225, 347, 47, 600, opacity=30, fill='white'),
        Star(250, 353, 51, 600, opacity=40, fill='white')
        )
    mist.width = 600
