app.stepsPerSecond = 0.5
l1=Rect(280,200,20,20,fill='blue')
l2=Rect(200,220,20,20,fill='blue')
l3=Rect(220,320,20,20,fill='blue')
l3=Rect(180,300,20,20,fill='blue')
l3=Rect(80,240,20,20,fill='blue')
l3=Rect(100,100,20,20,fill='lightGreen')







p1=Rect(280,360,20,20)
p2=Line (290,360,280,380,fill='brown')
p3=Line (290,360,300,380,fill='brown')
player=Group(p1,p2,p3)
#Player and Level Test variables
player.xv=0
player.lv=0
#Player calculated distance variable
player.mv=0
#Player Velocity variables
player.vx=0
player.yx=0
player.direction = 0
def onStep():
    player.centerX += player.vx
    player.centerY += player.yx
    if player.direction ==('up'):
        player.vx -=0.5
def onKeyPress(k):
    #Player controler for testing
    if k == ('w'):
        player.centerY +=-20
        player.rotateAngle=0
    if k == ('s'):
      player.centerY +=20
      player.rotateAngle=180
    if k == ('d'):
      player.centerX+=20
      player.rotateAngle=90
    if k == ('a'):
        player.centerX +=-20
        player.rotateAngle=270
    #Function test
    if k ==('c'):
        player.direction = "up"
    if k ==('space'):
        if player.centerX == l1.centerX:
            player.xv = player.centerY
            player.lv = l1.centerY
            #Print initial x coord
            print (player.lv)
            print (player.xv)
            #Check if level coord is bigger than player coord, if so set player calculated move variable to lv-xv, then print calculated move
            if player.lv > player.xv:
                player.mv = player.lv-player.xv
                print (player.mv)
            #If xv is bigger, caluclate xv-lv instead
            if player.lv < player.xv:
                player.mv = player.xv-player.lv
                print (player.mv)
            #Divide total move by 10, to create animation, then print numbers into console
            player.mv = player.mv/20
            print (player.mv)
            #If player is above level, increase x by 20, otherwise decrease x by 20
            while player.mv>1:
                if player.lv > player.xv:
                    player.centerY +=20
                    player.mv=player.mv-1
                    player.rotateAngle = 180
                if player.lv < player.xv:
                    player.centerY +=-20
                    player.mv=player.mv-1
                    player.rotateAngle = 0
        if player.centerY == l1.centerY:
            player.xv = player.centerX
            player.lv = l1.centerX
            #Print initial y coord
            print (player.lv)
            print (player.xv)
            #Check if level coord is bigger than player coord, if so set player calculated move variable to lv-xv, then print calculated move
            if player.lv > player.xv:
                player.mv = player.lv-player.xv
                print (player.mv)
            #If xv is bigger, caluclate xv-lv instead
            if player.lv < player.xv:
                player.mv = player.xv-player.lv
                print (player.mv)
            #Divide total move by 10, to create animation, then print numbers into console
            player.mv = player.mv/20
            print (player.mv)
            #If player is above level, increase x by 20, otherwise decrease x by 20
            while player.mv>1:
                if player.lv > player.xv:
                    player.centerX +=20
                    player.mv=player.mv-1
                    player.rotateAngle = 90
                if player.lv < player.xv:
                    player.centerX +=-20
                    player.mv=player.mv-1
                    player.rotateAngle = -90
        
            
def onKeyRelease(key):
    player.direction = None
Label("wasd for movement, and press space to test distance calculation",200,20)           
           
            
