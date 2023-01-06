app.background = gradient(rgb(0, 30, 0), 'darkGreen', start='bottom')
# draw the flytrap and its flowerpot
Polygon(100, 250, 150, 400, 250, 400, 300, 250,
        fill=gradient('darkRed', 'fireBrick', start='left'))
Oval(200, 250, 200, 80, fill='sienna', border='darkRed', borderWidth=4)
Oval(200, 200, 30, 150, fill=gradient('limeGreen', 'mediumSeaGreen', start='left'),
     rotateAngle=10)
Oval(190, 260, 50, 35, fill='saddleBrown')
Oval(190, 270, 70, 15, fill='sienna')
flytrap1 = Oval(195, 120, 35, 60, fill=gradient('crimson', 'salmon'),border='limeGreen', borderWidth=4, rotateAngle=-15)
flytrap2 = Oval(230, 120, 35, 60, fill=gradient('crimson', 'salmon'),border='limeGreen', borderWidth=4, rotateAngle=10)
# fly
flyWings = Oval(100, 200, 15, 20, fill='darkGray')
fly = Oval(100, 200, 20, 12)
fly.isEaten = False
def close():
    # This traps the fly.
    flytrap1.width = 25
    flytrap1.centerX = 205
    flytrap1.fill = gradient('mediumSeaGreen', 'limeGreen')
    flytrap2.width = 25
    flytrap2.centerX = 215
    flytrap2.fill = gradient('mediumSeaGreen', 'limeGreen')
    flyWings.visible = False
    fly.visible = False
    fly.isEaten = True
def onMouseMove(mouseX, mouseY):
    # The fly should only be moved to the mouse if it hasn't already been eaten.
    ### Fix Your Code Here ###
    flyWings.centerX = mouseX
    flyWings.centerY = mouseY
    fly.centerX = mouseX
    fly.centerY = mouseY
    # The flytrap should eat the fly whenever the fly flies into its mouth.
    ### Place Your Code Here ###
    if fly.hitsShape(flytrap1) or fly.hitsShape(flytrap2)==True:
        close()
