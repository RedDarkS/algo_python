xBall = 0
yBall = 0

ballColl = False
ratio = 0

xRack = 0
yRack = 0

xspdB = 0.25
yspdB = 0.15

ballSpeed = 1
ballAngle = random(PI/6, 3*PI/6)
angleMax = PI/1.9

recHeight = 20
recWidth = 100

xBrick = 250
yBrick = 250
brickWidth = 50
brickHeight = 30

sizeBall = 10

listBrick = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,]
nbBricks = 1

dt = 0
lastFrameTime = 0

def setup():
    global xBall, yBall, xRack, yRack
    
    size(500,500)
    clear()
    frameRate(60)
    
    xBall = width / 2
    yBall = height / 3

    xRack = width / 2
    yRack = height - 40
    
    
def draw():
    global lastFrameTime, dt
    
    clear()
    fill(255)

    drawRacket()
    drawBall()
    
    for i in range(len(listBrick)):
        if (listBrick[i] > 0):
            
            drawBricks(i*50, 50, 50, 20, i)
    
    coll()
    
    dt = millis() - lastFrameTime
    lastFrameTime = millis()


def drawRacket():
    global xRack, yRack, recWidth, recHeight
    rect(xRack, yRack, recWidth, recHeight)
    
    xRack = mouseX - recWidth/2
    
def drawBall():
    global xBall, yBall, xspdB, yspdB, sizeBall, dt, ballAngle, ballSpeed
    circle(xBall, yBall, 2*sizeBall)
    
    xBall += cos(ballAngle) * xspdB * dt
    yBall += sin(ballAngle) * yspdB * dt
    
def drawBricks(xBrick, yBrick, brickWidth, brickheight, index):
    global xBall, yBall, sizeBall, xspdB, yspdB, ballAngle, listBrick
    
    fill(255)

    rect(xBrick, yBrick, brickWidth, brickHeight)
    
    #collision bricks
    
    if xBrick <= xBall < xBrick + brickWidth:
        
        #haut
        if yBrick < yBall + sizeBall < yBrick + brickHeight and yspdB < 0:
            ballAngle = -ballAngle
            yBall = yBrick + sizeBall
            listBrick[index] = 0
        
        #bas
        elif yBrick < yBall - sizeBall < yBrick + brickHeight and yspdB > 0:
            ballAngle = -ballAngle
            yBall = yBrick + brickHeight + sizeBall
            listBrick[index] = 0
            
    elif yBrick <= yBall < yBrick + brickHeight:
        
        #gauche
        if xBrick < xBall + sizeBall < xBrick + brickWidth and xspdB > 0:
            ballAngle = PI -ballAngle
            xBall = xBrick - sizeBall
            listBrick[index] = 0
        
        #droite
        elif xBrick < xBall - sizeBall < xBrick + brickWidth and xspdB < 0:
            ballAngle = PI -ballAngle
            xBall = xBrick + brickWidth + sizeBall
            listBrick[index] = 0
        
    
        
def coll():
    global xBall, yBall, xRack, yRack, xspdB, yspdB, recWidth, recHeight, sizeBall, ballAngle, ballColl, ratio, angleMax, brickWidth, brickHeight
    
    #collision mur verticaux
    
    if xBall + sizeBall > width:
        ballAngle = PI - ballAngle
        #xBall + width-sizeBall
    elif xBall - sizeBall < 0 :
        ballAngle = PI - ballAngle
        #xBall = sizeBall
        
    #collision mur haut et bas
    
    if yBall - sizeBall < 0:
        ballAngle = -ballAngle
        #yBall = sizeBall
    elif (yBall + sizeBall > height):
        ballAngle = -ballAngle
        
    #collision côtés horizontaux de la barre
    
    if (yRack + recHeight > yBall + sizeBall > yRack) and (yspdB > 0):
        if (xBall > xRack) and (xBall < xRack + recWidth):
            if(xRack < xBall < xRack + recWidth):
                ratio = (xBall - xRack - (recWidth/2)) / (recWidth/2)
                ballAngle = -ballAngle - ratio * angleMax
                yBall = yRack - sizeBall
