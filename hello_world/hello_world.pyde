xBall = 0
yBall = 0

ballColl = False
ratio = 0

xRack = 0
yRack = 0

xspdB = 0.25
yspdB = 0.15

ballSpeed = 1
ballAngle = random(0, PI)
angleMax = PI/1.9

recHeight = 20
recWidth = 100

sizeBall = 10

listBrick = []
nbBricks = 1

dt = 0
lastFrameTime = 0

def setup():
    global xBall, yBall, xRack, yRack
    
    size(500,500)
    clear()
    frameRate(60)
    
    xBall = width / 2
    yBall = height / 2

    xRack = width / 2
    yRack = height - 40
    
    
def draw():
    global lastFrameTime, dt
    
    clear()
    fill(255)

    drawRacket()
    drawBall()
    
    ballColl = False
    
    coll()
    
    dt = millis() - lastFrameTime
    lastFrameTime = millis()


def drawRacket():
    global xRack, yRack, recWidth, recHeight
    barre = rect(xRack, yRack, recWidth, recHeight)
    
    xRack = mouseX - recWidth/2
    
def drawBall():
    global xBall, yBall, xspdB, yspdB, sizeBall, dt, ballAngle, ballSpeed
    balle = circle(xBall, yBall, 2*sizeBall)
    
    xBall += cos(ballAngle) * xspdB * dt
    yBall += sin(ballAngle) * yspdB * dt
        
def coll():
    global xBall, yBall, xRack, yRack, xspdB, yspdB, recWidth, recHeight, sizeBall, ballAngle, ballColl, ratio, angleMax
    
    #collision mur verticaux
    
    if xBall + sizeBall > width:
        ballAngle = PI - ballAngle
        xBall + width-sizeBall
    elif xBall - sizeBall < 0 :
        ballAngle = PI - ballAngle
        xBall = sizeBall
        
    #collision mur haut et bas
    
    if yBall - sizeBall < 0:
        ballAngle = -ballAngle
        yBall = sizeBall
    elif (yBall + sizeBall > height):
        ballAngle = -ballAngle
        
    #collision côtés horizontaux de la barre
    
    if (yRack + recHeight > yBall + sizeBall > yRack) and (yspdB > 0):
        if (xBall > xRack) and (xBall < xRack + recWidth):
            ballAngle = -ballAngle
            yBall = yRack - sizeBall
            ballColl = True
            
        #détection coordonnées

        if(ballColl is True):
            ratio = (xBall - xRack) / recWidth
            print (ratio)
            if(xRack < ratio < recWidth/2):
                ballAngle = -ballAngle * ratio
                ballColl = False
            elif ratio == recWidth/2:
                ballAngle = -ballAngle
                ballColl = False
            elif(recWidth/2 < ratio < recWidth):
                ballAngle = -ballAngle * ratio
                ballColl = False
            else:
                ballColl = False
                
                """
                if ratio < 50 :
                    angle =  (PI - ( (PI/2) * (ratio/50) ) ) 

                elif ratio > 50 :
                    angle = ( (PI/2) - ((PI/2)/(ratio/100)) )*-1
                """
    
