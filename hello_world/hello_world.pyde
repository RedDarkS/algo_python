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

xBrick = 250
yBrick = 250
brickWidth = 200
brickHeight = 50

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
    yBall = 10
    #height / 2

    xRack = width / 2
    yRack = height - 40
    
    
def draw():
    global lastFrameTime, dt
    
    clear()
    fill(255)

    drawRacket()
    drawBall()
    drawBricks()
    
    ballColl = False
    
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
    
def drawBricks():
    global xBall, yBall, sizeBall, xspdB, yspdB, ballAngle
    
    fill(255)

    rect(xBrick, yBrick, brickWidth, brickHeight)
        
    
        
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
    
    #collision bricks

    #Dessous
    if yspdB < 0 and (yBrick > yBall > yBrick + brickHeight):
        if xBrick + brickWidth > xBall > xBrick:
            print("tape dessous")
            ballAngle = -ballAngle
    
    #Dessus
    if yspdB > 0 and (yBrick < yBall < yBrick + brickHeight):
        if xBrick + brickWidth > xBall > xBrick:
            print("tape dessus")
            ballAngle = -ballAngle
    
    #Droite
    if yspdB != 0 and (yBrick < yBall < yBrick + brickHeight):
        if xBrick > xBall > xBrick + brickWidth:
            print("tape droite")
            ballAngle = PI - ballAngle
    
    #Gauche
    if yspdB != 0 and (yBrick < yBall < yBrick + brickHeight):
        if xBrick + brickWidth < xBall < xBrick:
            print("tape gauche")
            ballAngle = PI - ballAngle
    
