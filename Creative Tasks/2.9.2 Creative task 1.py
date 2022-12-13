import math
app.stepsPerSecond = 120
pmass = Label('',85,10)
bmass = Label('',75,25)
Label('Player Mass:',40,10)
Label('Ball Mass:',33,25)
Label('Press 1 to change the player mass, 2 for the ball mass',150,390)
#Player and all player variables
player=Circle(200,300,20,fill='white',border='black')
player.xv = 0
player.yv = 0
player.mass = player.radius
player.lastMouseX = 0
player.lastMouseY = 0
player.v1 = 0
player.v1n = 0
player.v1np = 0
player.v1t = 0
player.v2tp = 0
player.vp = 0
player.isdigit = 0
#Other shape variables (Ball)
ball = Circle(200,100,20)
ball.mass = ball.radius
ball.xv = 0
ball.yv = 0
ball.v2 = 0
ball.v2n = 0
ball.v2np = 0
ball.v2t = 0
ball.v2tp = 0
ball.vp = 0
ball.isdigit = 0
#Variables associated with both the player and shape
handle = Polygon()
handle.vn = 0
handle.un = 0
handle.ut = 0
#Mouse Pointer
mouseLine = Line(player.centerX,player.centerY,player.centerX,player.centerY)
pointer = Polygon(200,100,195,110,205,110)
pointer.visible=False
player.toFront()
def collide(playerMass,ballMass):
    player.mass = playerMass
    ball.mass = ballMass
    #Find normal vector(handle.vn)
    handle.vn = [player.centerX - ball.centerX, player.centerY - ball.centerY]
    # print(handle.vn)
    #Find unit vector of handle.vn (handle.un)
    handle.un = [handle.vn[0]/math.sqrt(handle.vn[0]**2 + handle.vn[1]**2), handle.vn[1]/math.sqrt(handle.vn[0]**2 + handle.vn[1]**2)]
    # print(handle.un)
    #Find unit tangent vector(handle.ut)
    handle.ut = [-handle.un[1], handle.un[0]]
    # print(handle.ut)
    #Create initial velocity vectors(player.v1, ball.v2)
    player.v1 = [player.xv, player.yv]
    ball.v2 = [ball.xv, ball.yv]
    #Resolve velocity vectors into normal tangential
    player.v1n = handle.un[0]*player.v1[0] + handle.un[1] * player.v1[1]
    player.v1t = handle.ut[0] * player.v1[0] + handle.ut[1] * player.v1[1]
    ball.v2n = handle.un[0]*ball.v2[0] + handle.un[1] * ball.v2[1]
    ball.v2t = handle.ut[0] * ball.v2[0] + handle.ut[1] * ball.v2[1]
    # print(player.v1n)
    # print(player.v1t)
    # print(ball.v2n)
    # print(ball.v2t)
    #Find new normal velocities
    player.v1np = ((player.v1n*(player.mass - ball.mass)) + 2 * ball.mass * ball.v2n)/(player.mass + ball.mass)
    ball.v2np = ((ball.v2n*(ball.mass - player.mass)) + 2 * player.mass*player.v1n)/(player.mass + ball.mass)
    # print (player.v1np)
    # print (ball.v2np)
    #Convert scalar normal and tangential velocities into vectors
    player.v1np = [player.v1np * handle.un[0], player.v1np * handle.un[1]]
    player.v1tp = player.v1t * handle.ut[0], player.v1t * handle.ut[1]
    ball.v2np = [ball.v2np * handle.un[0], ball.v2np * handle.un[1]]
    ball.v2tp = ball.v2t * handle.ut[0], ball.v2t * handle.ut[1]
    # print(player.v1np)
    # print(ball.v2np)
    #Find final velocities vectors by adding the normal and tangential componenets for each objects
    player.vp = player.v1np[0] + player.v1tp[0], player.v1np[1] + player.v1tp[1]
    ball.vp = ball.v2np[0] + ball.v2tp[0], ball.v2np[1] + ball.v2tp[1]
    # print(player.vp)
    # print(ball.vp)
    # print('__________________________________')
    #Set the x and y velocities based on final vectors
    player.xv = player.vp[0]
    player.yv = player.vp[1]
    ball.xv = ball.vp[0]
    ball.yv = ball.vp[1]
          
def onMouseDrag(x,y):
    #Aim the player
    mouseLine.visible=True
    mouseLine.x2=x
    mouseLine.y2=y
    pointer.visible=True
    pointer.centerX=x
    pointer.centerY=y
    player.lastMouseX = x
    player.lastMouseY = y
    
def onMouseRelease(x,y):
    #Set player x and y velocities based on the player x,y and the mouse x,y
    player.lastMouseX = x
    player.lastMouseY = y
    player.xv = pythonRound((x - player.centerX),1)/60
    player.yv = pythonRound((y - player.centerY),1)/60
    mouseLine.visible=False
    pointer.visible=False

def onKeyPress(key):
    #User input to modify player and ball mass
    if key == '1':
        massa = app.getTextInput('Input Player Mass from 1-50')
        #Checks if user input is a number, then if the value is within 1-50
        player.isdigit = massa.isdigit()
        if  player.isdigit == True and int(massa)<51:
            player.radius = int(massa)
            player.mass = int(massa)
            print('Set!')
        #If not, print Either not a number or within 1-50 and mass remains the same
        else:
            player.isdigit = False
            player.mass = player.mass
        print("Either not a number or within 1-50")
    #Same to the ball
    if key == '2':
        massb = app.getTextInput('Input Ball Mass from 1-50')
        ball.isdigit = massb.isdigit()
        if  ball.isdigit == True and int(massb)<51:
            ball.radius = int(massb)
            ball.mass = int(massb)
            print('Set!')
        else:
            ball.isdigit = "Either not a number or within 1-50"
            ball.mass = ball.mass
            print("Either not a number or within 1-50")
    else:
        pass

def onStep():
    pointer.rotateAngle=angleTo(player.centerX,player.centerY,player.lastMouseX,player.lastMouseY)
    #Adjusts values so that visuals match variables
    ball.mass = ball.radius
    player.mass = player.radius
    pmass.value = (player.mass)
    bmass.value = (ball.mass)
    if player.hitsShape(ball):
        collide(pmass.value, bmass.value)
    mouseLine.x1=player.centerX 
    mouseLine.y1=player.centerY
    #Moves player and ball by calculated velocity vectors  
    player.centerX += player.xv
    player.centerY += player.yv
    ball.centerX += ball.xv
    ball.centerY += ball.yv
    #Bounce Back if touching a border
    if player.centerX >400 - player.radius:
        player.xv = -player.xv
    if player.centerX <0 + player.radius:
        player.xv = -player.xv
    if player.centerY >400 - player.radius:
        player.yv = -player.yv
    if player.centerY < 0 + player.radius:
        player.yv = -player.yv
    if ball.centerX >400 - ball.radius:
        ball.xv = -ball.xv
    if ball.centerX <0 + ball.radius:
        ball.xv = -ball.xv
    if ball.centerY >400 -  ball.radius:
        ball.yv = -ball.yv
    if ball.centerY <0+ball.radius:
        ball.yv = -ball.yv
    if player.centerX > 400-player.radius:
        player.centerX -=player.radius        
