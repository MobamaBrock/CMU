app.background = gradient('lightSalmon', 'lightCoral', 'mediumOrchid', start='bottom')
# water
Oval(20, 400, 400, 170, fill=gradient('cornflowerBlue', 'royalBlue', start='top'))
Oval(350, 403, 400, 165, fill=gradient('cornflowerBlue', 'royalBlue', start='top'))
Oval(200, 405, 450, 160, fill=gradient('cornflowerBlue', 'royalBlue', start='top'))
# water drops
Circle(180, 290, 10, fill='white')
Circle(200, 305, 5, fill='white')
Circle(190, 315, 3, fill='white')
Circle(295, 300, 10, fill='white')
Circle(305, 320, 5, fill='white')
Circle(315, 310, 3, fill='white')
Circle(360, 295, 8, fill='white')
Circle(375, 310, 3, fill='white')
Circle(395, 295, 3, fill='white')
# dolphins
dolphin1 = Polygon(60, 105,  95, 110, 140, 105, 130, 130, 170, 155, 195, 200,
                   200, 240, 230, 290, 195, 265, 170, 275, 185, 250, 160, 215,
                   120, 185,  115, 225,  85, 165,  15, 120,  20, 110,  40, 115,
                   fill=gradient('whiteSmoke', 'gainsboro', start='top'))
dolphin2 = Polygon(155, 105, 190, 110, 235, 105, 225, 130, 265, 155, 290, 200,
                   295, 240, 325, 290, 290, 265, 265, 275, 280, 250, 255, 215,
                   215, 185,  210, 225, 180, 165, 110, 120, 115, 110, 135, 115,
                   fill=gradient('lightSkyBlue', 'deepSkyBlue', start='top'))
dolphin3 = Polygon(260, 105, 295, 110, 340, 105, 330, 130, 370, 155, 395, 200,
                   400, 240, 430, 290, 395, 265, 370, 275, 385, 250, 360, 215,
                   320, 185, 315, 225, 285, 165, 215, 120, 220, 110, 240, 115,
                   fill=gradient('mediumSlateBlue', 'slateBlue', start='top'))
# hoop
hoop = Oval(120, 145, 50, 200, fill=None, borderWidth=10,
            border=gradient('gold', 'lightGreen', 'gold', 'lightGreen', 'gold',
                            start='top'))
dolphin2.toFront()
def b(dolphin):
    # Bring the hoop and the dolphin to the front.
    ### Place Your Code Here ###
    ### (HINT: The center of the hoop should be 10 pixels to the right of the
    #          dolphin's leftmost point!)
    ### Place Your Code Here ###
    hoop.centerX = dolphin.left + 10
    hoop.toFront()
    dolphin.toFront()
def onMousePress(x,y):
    # When you click on a dolphin, the dolphin is brought to the front and
    # it is ready to jump through the hoop!
    ### (HINT: Use the helper function we defined above. What argument should
    #.         you pass into the function?)
    ### Place Your Code Here ###
    if dolphin1.hits(x,y)==True:
        b(dolphin1)
    elif dolphin2.hits(x,y)==True:
        b(dolphin2)
    elif dolphin3.hits(x,y)==True:
        b(dolphin3)
