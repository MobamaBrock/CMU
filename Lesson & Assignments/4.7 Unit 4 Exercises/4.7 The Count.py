app.background = rgb(30, 60, 150)

# moon
Circle(300, 100, 60, fill='white')
Circle(290, 90, 60, fill=rgb(30, 60, 150))

# tree
Line(0, 110, 100, 100, fill=rgb(60, 20, 10), lineWidth=10)
Line(100, 100, 170, 125, fill=rgb(60, 20, 10), lineWidth=6)
Line(100, 98, 185, 80, fill=rgb(60, 20, 10), lineWidth=7)
Line(185, 80, 205, 50, fill=rgb(60, 20, 10), lineWidth=3)
Line(185, 80, 220, 100, fill=rgb(60, 20, 10), lineWidth=3)
Line(170, 125, 195, 115, fill=rgb(60, 20, 10), lineWidth=3)
Line(170, 125, 180, 140, fill=rgb(60, 20, 10), lineWidth=3)

# bat body
Polygon(100, 190, 50, 215, 150, 215, fill='crimson')
Polygon(100, 100, 135, 190, 100, 230, 65, 190)
Polygon(90, 205, 110, 205, 100, 170, fill='white')
Polygon(90, 190, 90, 200, 110, 190, 110, 200, fill='crimson')
Circle(100, 195, 3, fill='crimson')

# bat head
Polygon(100, 220, 60, 255, 140, 255, fill='pink', border=rgb(20, 20, 20))
Circle(100, 230, 28, fill=rgb(20, 20, 20))
Circle(95, 245, 2, fill='white')
Circle(105, 245, 2, fill='white')
Oval(100, 225, 25, 10, fill='white')
Polygon(94, 222, 96, 215, 98, 222, fill='white')
Polygon(106, 222, 104, 215, 102, 222, fill='white')
Circle(95, 247, 2, fill=rgb(20, 20, 20))
Circle(105, 247, 2, fill=rgb(20, 20, 20))
Oval(100, 227, 25, 10, fill=rgb(20, 20, 20))

# thought bubble
Circle(135, 270, 4, fill='white')
Circle(150, 285, 8, fill='white')
Circle(180, 295, 10, fill='white')
Circle(240, 315, 45, fill='white', border='gainsboro', borderWidth=3)
Circle(290, 290, 35, fill='white', border='gainsboro', borderWidth=3)
Circle(330, 320, 40, fill='white', border='gainsboro', borderWidth=3)
Circle(280, 335, 40, fill='white', border='gainsboro', borderWidth=3)
Rect(225, 285, 100, 65, fill='white')

Label('The Count counts...', 285, 310, font='monospace')
text = Label('(click the screen)', 285, 330, font='monospace')

def onMousePress(mouseX, mouseY):
    vowels = 'aeiouAEIOU'
    vowelsNum = 0
    message = app.getTextInput()
    
    for i in range(len(message)):
        if message[i] in vowels:
            print("hi")
            vowelsNum += 1
            
    print(vowelsNum)
    text.value = str(vowelsNum) + ' vowels!'
