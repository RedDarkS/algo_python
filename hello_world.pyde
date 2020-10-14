xBall = 0
yBall = 0

xRack = 0
yRack = 0

xspdB = 5
yspdB = 3

recHeight = 20
recWidth = 100

sizeBall = 10

listBrick = []
nbBricks = 1

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
    clear()
    fill(255)
    
    drawRacket()
    drawBall()
    coll()

def drawRacket():
    global xRack, yRack, recWidth, recHeight
    barre = rect(xRack, yRack, recWidth, recHeight)
    
    xRack = mouseX - recWidth/2
    
def drawBall():
    global xBall, yBall, xspdB, yspdB, sizeBall
    balle = circle(xBall, yBall, 2*sizeBall)
    
    xBall += xspdB
    yBall += yspdB
        
def coll():
    global xBall, yBall, xRack, yRack, xspdB, yspdB, recWidth, recHeight, sizeBall
    
    #collision mur verticaux
    
    if xBall + sizeBall > width:
        xspdB *= -1
        xBall + width-sizeBall
    elif xBall - sizeBall < 0 :
        xspdB *= -1
        xBall = sizeBall
        
    #collision mur haut et bas
    
    if yBall - sizeBall < 0:
        yspdB *= -1
        yBall = sizeBall
    elif (yBall + sizeBall > height):
        yspdB *= -1
        
    #collision côtés horizontaux de la barre
    
    if (yRack + recHeight > yBall + sizeBall > yRack) and (yspdB > 0):
        if (xBall > xRack) and (xBall < xRack + recWidth):
            yspdB *= -1
            yBall = yRack - sizeBall
    #if ((xRack <= xBall + sizeBall <= xRack + recWidth) and (yBall + sizeBall >= yRack) and (yBall + sizeBall <= yRack + recHeight)):
    #    yspdB *= -1
    
    #collision côtés verticaux de la barre
    
    #if ((xRack <= xBall + sizeBall) and (yRack + recHeight >= yBall >= yRack)) or ((xBall - sizeBall <= xRack + recWidth) and (yRack + recHeight >= yBall >= yRack)): 
    #    xspdB *= -1
    
