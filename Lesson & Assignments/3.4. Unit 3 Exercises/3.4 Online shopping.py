app.background = 'azure'

app.books = [ ]

# bag
Circle(350, 40, 8, fill=None, border='black'),
Rect(350, 55, 30, 30, fill='yellow', border='black', align='center'),
bagLabel = Label(0, 350, 55, size=16)

# website layout
Circle(110, 60, 7, fill=None, border='darkGrey')
Line(115, 65, 120, 70, fill='darkGrey')
Rect(125, 50, 150, 20, fill='white', border='darkGrey')
Label('books on programming', 200, 60)
Label('Code & Noble', 200, 20, italic=True, size=25)

def generateBook(cx, cy, color, name, label1, label2):
    book = Group(
        # background
        Rect(40, 80, 130, 140, fill='gray', opacity=30),
        Rect(50, 70, 130, 140, fill='white', border='black'),
        Rect(50, 190, 130, 20, fill='yellow', border='black'),
        Label('Add To Bag', 115, 200),

        # book
        Rect(85, 85, 70, 90, fill=color),
        Polygon(85, 85, 70, 90, 70, 180, 85, 175),
        Polygon(70, 180, 85, 175, 155, 175, 150, 180, fill='white', border='black'),
        Line(90, 155, 150, 155),
        Label(label1, 120, 115),
        Label(label2, 120, 130)
        )
    book.centerX = cx
    book.centerY = cy
    app.books.append(book)

generateBook(115, 160, 'limeGreen', 'Coding Games', 'Coding', 'Games')
generateBook(295, 160, 'turquoise', 'The Code Thief', 'The Code', 'Thief')
generateBook(115, 320, 'tomato', 'Mostly Bugless', 'Mostly', 'Bugless')
generateBook(295, 320, 'gold', "Charlotte's Website", "Charlotte's", 'Website')

def displaySoldOut(x, y):
    Rect(x, y, 130, 140, fill='dimGrey', opacity=60, align='center')
    Label('SOLD OUT', x, y, fill='white', size=18, bold=True, rotateAngle=-30)
app.books[0].hit = False
app.books[1].hit = False
app.books[2].hit = False
app.books[3].hit = False
def onMousePress(mouseX, mouseY):
    # If any of the books are clicked on, it should become sold out and the
    # bag counter should increase by 1.
    ### (HINT: The books are stored in app.books. Make sure that this list is
    #          updated so we can't click on books that are sold out!)
    if app.books[0].hits(mouseX,mouseY):
        if app.books[0].hit == False:
            displaySoldOut(50+65,90+70)
            app.books[0].hit = True
            bagLabel.value +=1
    if app.books[1].hits(mouseX,mouseY):
        if app.books[1].hit == False:
            displaySoldOut(230+65,90+70)
            app.books[1].hit = True
            bagLabel.value += 1
    if app.books[2].hits(mouseX,mouseY):
        if app.books[2].hit == False:
            displaySoldOut(50+65,250+70)
            app.books[2].hit = True
            bagLabel.value += 1
    if app.books[3].hits(mouseX,mouseY):
        if app.books[3].hit == False:
            displaySoldOut(230+65,250+70)
            app.books[3].hit = True
            bagLabel.value += 1
