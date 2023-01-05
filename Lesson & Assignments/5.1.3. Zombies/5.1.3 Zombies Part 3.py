import random

app.background = 'gold'

infectedZone = Rect(0, 0, 1, 400, fill='crimson')
people = []

def drawPerson(cx, cy):
    # Randomly assign if the person is immune or not, and if they are draw
    # a blue "halo" behind them.
    isImmuneOptions = random.randint(0,1)
    if isImmuneOptions == 0:
        immuneCircle = Circle(cx, cy, 25, fill='skyBlue')
        head = Circle(cx, cy, 20, fill='tan')
        person = Group(
        immuneCircle,
        head,
        Circle(cx + 8, cy - 5, 2),
        Circle(cx - 8, cy - 5, 2),
        Circle(cx, cy + 5, 5)
        )
        person.head = head
        person.isImmune = True

    else:
        head = Circle(cx, cy, 20, fill='tan')
        person = Group(
        head,
        Circle(cx + 8, cy - 5, 2),
        Circle(cx - 8, cy - 5, 2),
        Circle(cx, cy + 5, 5)
        )
        person.head = head
        person.isImmune = False

    people.insert(0,person)

def createPeople():
    for i in range(15):
        drawPerson(random.randint(0,400), random.randint(0,400))
    # Create 15 people randomly positioned in the canvas.
    pass


def moveInfectedZone(x):

    # If we clicked to the right of the infected zone's right edge, increase the
    # width of the infected zone to be 1 pixel more than the x position.
    if x > infectedZone.centerX*2:
        infectedZone.width = x+1
    pass


    # If the infected zone is further right than a non-immune person's left
    for i in range(len(people)):
        print(people[i].isImmune)
        if people[i].isImmune == False and infectedZone.right > people[i].left:
            people[i].head.fill = 'green'
    # edge, that person's head should become green.
    ### Place Your Code Here ###


def onMousePress(mouseX, mouseY):
    moveInfectedZone(mouseX)
        
    # Call the moveInfectedZone function with the mouse's position as an argument.
    pass
