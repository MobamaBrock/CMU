app.background = 'white'
app.backgrounds = [ 'white', 'lightYellow', 'lemonChiffon', rgb(255, 240, 190) ]
app.backgroundIndex = 0

# floor
Polygon(0, 340, 400, 340, 400, 400, 0, 400, fill='tan', opacity=50)

# table
Polygon(200, 250, 400, 220, 400, 400, 380, 400, fill='wheat')
Polygon(200, 250, 200, 260, 365, 400, 380, 400, 320, 350, fill='burlyWood')
Polygon(220, 277, 320, 360, 220, 370, fill=rgb(230, 200, 155))

# book
Polygon(370, 260, 400, 260, 400, 330, 370, 330, fill='oliveDrab')
Polygon(370, 260, 375, 260, 375, 330, 370, 330, fill=rgb(80, 40, 20))
Polygon(375, 255, 385, 255, 385, 270, 380, 280, 375, 270, fill='forestGreen')

# picture frame
Polygon(40, 50, 90, 50, 90, 100, 40, 100, fill=None, border='seaGreen',
        borderWidth=5)
Polygon(50, 60, 80, 60, 80, 90, 50, 90,
        fill=gradient('tan', 'seaGreen', start='left'))

# legs
Polygon(270, 235, 195, 245, 195, 300, 185, 300, 190, 305, 200, 305, 200, 250,
        270, 240, fill=rgb(160, 110, 75))
Polygon(185, 300, 185, 315, 190, 320, 190, 305, fill=rgb(80, 40, 20))
Polygon(190, 305, 190, 320, 220, 320, 220, 247, 200, 250, 200, 305,
        fill='tan')
Polygon(220, 267, 270, 260, 270, 240, 220, 247, fill='tan')
Polygon(270, 235, 300, 263, 230, 275, 230, 325, 220, 325, 215, 320, 225, 320,
        225, 270, 292, 260, 270, 240, fill=rgb(160, 110, 75))
Polygon(270, 240, 270, 260, 275, 263, 292, 260, fill=rgb(150, 115, 75))
Polygon(215, 320, 215, 335, 220, 340, 220, 325, fill=rgb(90, 70, 50))
Polygon(220, 340, 250, 340, 250, 270, 230, 275, 230, 325, 220, 325,
        fill='tan')
Polygon(250, 270, 250, 290, 300, 283, 300, 263, fill='tan')

# body
Polygon(275, 242, 285, 250, 285, 190, 275, 182, fill=rgb(190, 155, 105))
Polygon(285, 190, 285, 250, 297, 259, 297, 190, fill='tan')
Polygon(275, 182, 252, 138, 258, 140, 285, 190, fill=rgb(150, 115, 75))
Polygon(258, 140, 285, 190, 297, 190, 268, 135, fill=rgb(190, 155, 105))

# bulb
Oval(250, 120, 100, 50, fill='white', border='tan', rotateAngle=-15)
Polygon(192, 120, 290, 120, 290, 50, 192, 50, fill='white', rotateAngle=-15)
Oval(232, 50, 100, 50, fill='white', border='tan', rotateAngle=-15)

light = Group(
    Oval(250, 120, 100, 50, border='tan', rotateAngle=-15),
    Polygon(192, 120, 290, 120, 290, 50, 192, 50, rotateAngle=-15),
    Oval(232, 50, 100, 50, border='tan', rotateAngle=-15),
    Arc(250, 118, 100, 50, 90, 180, rotateAngle=-15),
    Arc(232, 52, 100, 50, 270, 180, rotateAngle=-15)
    )
light.fill = rgb(255, 215, 70)
light.opacity = 10
lightme = [10,30,50,70]
app.index = 0
switchFrame = Group(
    Rect(100, 145, 40, 60, fill='wheat'),
    Circle(120, 160, 8, fill='dimGray'),
    Rect(120, 160, 16, 30, fill='dimGray', align='top'),
    Circle(120, 190, 8, fill='dimGray')
    )
switch = Circle(120, 160, 6, fill='white')
switchy = [160,170,180,190]
app.index = 1
app.backgroundIndex = 1
def onMousePress(mouseX, mouseY):
    if switch.hits(mouseX,mouseY) or switchFrame.hits(mouseX,mouseY):
            switch.centerY = switchy[app.index]
            app.background = app.backgrounds[app.backgroundIndex]
            light.opacity = lightme[app.index]
            app.backgroundIndex +=1
            app.index+=1
            app.index = app.index % 4
            app.backgroundIndex = app.backgroundIndex % 4
