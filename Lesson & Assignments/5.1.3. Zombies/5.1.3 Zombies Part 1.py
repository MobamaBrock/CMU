import random

app.background = 'gold'

people = Group()

def drawPerson(cx, cy):
    

    #### START OF BLOCK DRAW_PERSON ####

    # Randomly assign if the person is immune or not, and if they are draw
    # a blue "halo" behind them.
    ### (HINT: Make sure to add the halo to the person Group.)
    ### Place Your Code Here ###
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
    #### END OF BLOCK ####

    people.add(person)

def createPeople():
    #### START OF BLOCK CREATE_PEOPLE ####
    for i in range(15):
        drawPerson(random.randint(0,400), random.randint(0,400))
    # Create 15 people randomly positioned in the canvas.
    ### Place Your Code Here ###
    pass

    #### END OF BLOCK ####
