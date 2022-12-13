app.stepsPerSecond = 60
left = Rect(0,0,200,400,fill=rgb(16,114,185))
right = Rect(200,0,200,400,fill=rgb(229,20,32))
Label(app.getTextInput('Input First Selection'),100,200,size=30,fill = 'white')
Label(app.getTextInput('Input Second Selection'),300,200,size=30,fill = 'white')
Line(200,0,200,400,fill = 'white')
mouse = Circle(0,0,5,opacity=0)
votes = []
names = []
votesLeft = Label('',90,365,fill = 'white',size=30)
votesLeft.me = 0
votesRight = Label('',300,365,fill = 'white',size=30)
votesRight.me = 0
#A list for different values in this order: If the space bar is being pressed, index for opening or closing info screen, 
handles = [False,0,0,0,False]
def generateIp():
    return '.'.join(
        str(randrange(0,255)) for _ in range(4)
        )

def onKeyHold(key):
    if key == ['space']:
        handles[0] = True

def onKeyRelease(key):
    handles[0] = False

data = Group()
def identify(x,y,show):

    if handles[0] == True:
        for i in range(len(votes)):
            if votes[i].hits(x,y):
                handles[2] = i
                votes[handles[2]].toFront()
            else:
                i += 1
    if show == True:
        data.visible = True
        handles[1] = True
        data.add(Label(names[handles[2]],200,100,fill='white',size = 30))
        data.add(Label(names[handles[2] + 1],200,200,fill='white',size = 30))
        data.add(Label('Click again to close',80,15,fill='white',size = 15,bold = True))
        data.toFront()
    else:
        data.visible = False
        data.clear()
        
def onStep():
    if handles[4] == True:
        if handles[1] == True and votes[handles[2]].radius <= 400:
            handles[3] += 5
            votes[handles[2]].radius += handles[3]
        
        elif handles[1] == False and votes[handles[2]].radius != 5:
            votes[handles[2]].radius += -handles[3]
            handles[3] -= 5    
            identify(0,0,False)
            
def onMousePress(x,y):
    if handles[1] == True:    
        handles[1] = False
    else:
        if handles[0] != True:
            temp = app.getTextInput('Enter Your First and Last Name')
            if temp != '':
                names.append (temp)
                names.append(generateIp())
                if left.hits(x,y):
                    votes.append(Circle(x,y,5,fill=rgb(229,20,32)))
                    votes.append(Polygon())
                    votesLeft.me += 1
                    votesLeft.value = votesLeft.me
                if right.hits(x,y):
                    votes.append(Circle(x,y,5,fill=rgb(16,114,185)))
                    votes.append(Polygon())
                    votesRight.me += 1
                    votesRight.value = votesRight.me
                if handles[4] == False:
                    handles[4] = True
        else:
            identify(x,y,True)
