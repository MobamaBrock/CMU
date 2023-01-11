app.background = 'silver'

Label('Click on the pencil to add tasks!', 200, 390, size=16)

# clipboard
Rect(65, 25, 270, 350, fill='saddleBrown')
Rect(95, 55, 210, 290, fill='white')
Rect(165, 15, 70, 30)
Circle(200, 15, 15)
Label('TASKS', 200, 70, size=18)

tasks = Group()
tasks.labelY = 90
tasks.counter = 1

checkboxes = Group()

pencil = Group(
    Circle(280, 330, 4, fill='pink'),
    Polygon(320, 215, 330, 220, 330, 205),
    Line(280, 330, 325, 215, fill='gold', lineWidth=10)
    )

def tryCheckingBox(mouseX, mouseY):
    for checkbox in checkboxes:
        if (checkbox.hits(mouseX, mouseY) == True):
            Label('x', checkbox.centerX, checkbox.centerY)

def onMousePress(mouseX, mouseY):
    if (pencil.hits(mouseX, mouseY) == True):
        # Ask the user for a new task, then use their input to get a string that
        # is of the format 'taskNumber. newTaskHere', like shown in the test cases.
        ### Place Your Code Here ###
        newValue = app.getTextInput('task')
        tasks.add(
            Label(str(tasks.counter) +'. '+ newValue, 110, tasks.labelY, align='left', size=14)
            )
        checkboxes.add(
            Rect(270, tasks.labelY - 5, 10, 10, fill='white', border='black',
                 borderWidth=1)
            )
        tasks.labelY += 20
        tasks.counter += 1
        
    # See if any checkboxes were marked.
    tryCheckingBox(mouseX, mouseY)

##### Place your code above this line, code below is for testing purposes #####
# test case:
app.setTextInputs('Do homework', 'Cook food', 'Write essay', 'Code')
onMousePress(300, 280)
onMousePress(300, 280)
onMousePress(300, 280)
onMousePress(300, 280)
onMousePress(275, 110)
onMousePress(275, 150)
