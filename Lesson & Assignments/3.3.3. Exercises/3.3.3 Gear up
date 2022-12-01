app.background = 'lightCyan'

# index to keep track of the armor level
app.level = 0
app.armorColors = [
    None,
    gradient('peru', 'saddleBrown'),
    gradient(rgb(255, 240, 0),
    rgb(235, 180, 20)),
    gradient('snow', 'silver'),
    gradient('aqua', 'darkTurquoise'),
    gradient('dimGrey', rgb(60, 60, 60))
    ]

Rect(0, 300, 400, 100, fill='limeGreen')
Rect(310, 10, 80, 80, fill='gold', border='lightGoldenrodYellow', borderWidth=15)

# upgrade and downgrade buttons
Rect(260, 130, 100, 150, fill='darkGrey',
     border=gradient('white', 'dimGrey', start='left-top'), borderWidth=4)
upgradeButton = Group(
    Rect(280, 180, 60, 5), Rect(285, 175, 50, 5),
    Rect(290, 170, 40, 5), Rect(295, 165, 30, 5),
    Rect(300, 160, 20, 5), Rect(305, 155, 10, 5)
    )
upgradeButton.fill = gradient('dimGray', rgb(75, 75, 75), start='left-top')

downgradeButton = Group(
    Rect(280, 225, 60, 5), Rect(285, 230, 50, 5),
    Rect(290, 235, 40, 5), Rect(295, 240, 30, 5),
    Rect(300, 245, 20, 5), Rect(305, 250, 10, 5)
    )
downgradeButton.fill = gradient('dimGray', rgb(75, 75, 75), start='left-top')

# steve
Rect(80, 50, 80, 80, fill='burlyWood')
Rect(105, 130, 30, 10, fill='burlyWood')
Rect(40, 170, 160, 80, fill='burlyWood')
Polygon(80, 80, 80, 50, 160, 50, 160, 80, 150, 80, 150, 70,
        90, 70, 90, 80, fill=rgb(55, 20, 10))
Line(90, 95, 150, 95, fill='white', lineWidth=10, dashes=(10, 40))
Line(100, 95, 150, 95, fill='darkSlateBlue', lineWidth=10, dashes=(10, 20))
Rect(110, 100, 20, 10, fill=rgb(150, 30, 20), opacity=30)
Polygon(100, 110, 100, 130, 140, 130, 140, 110,
        130, 110, 130, 120, 110, 120, 110, 110, fill=rgb(55, 20, 10))
Polygon(40, 130, 105, 130, 105, 140, 135, 140, 135, 130, 200, 130, 200, 170,
        160, 170, 160, 230, 80, 230, 80, 170, 40, 170, fill='turquoise')
Rect(80, 230, 80, 120, fill='darkSlateBlue')

armor = Group(
    Polygon(75, 45, 165, 45, 165, 90, 150, 90, 150, 80, 130, 80, 130, 100,
            110, 100, 110, 80, 90, 80, 90, 90, 75, 90, fill=None),
    Polygon(40, 130, 105, 130, 105, 140, 135, 140, 135, 130, 200, 130, 200, 170,
            160, 170, 160, 230, 80, 230, 80, 170, 40, 170, fill=None),
    Rect(80, 230, 80, 120, fill=None)
    )

# detail lines
Line(120, 235, 120, 350, opacity=10)
Line(80, 130, 80, 170, opacity=10)
Line(160, 130, 160, 170, opacity=10)

def onMousePress(mouseX, mouseY):  
    
    if upgradeButton.hits(mouseX,mouseY):
        if app.level == 5:
            print('rest')
            app.level = 0
            armor.fill = app.armorColors[app.level]
        else:
            print('no')
            app.level += 1
            armor.fill = app.armorColors[app.level]
        
    if downgradeButton.hits(mouseX,mouseY):
        if app.level == 0:
            app.level = 5
        else:
            app.level -= 1
            armor.fill = app.armorColors[app.level]
