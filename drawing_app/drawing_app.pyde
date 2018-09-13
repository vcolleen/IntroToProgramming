#making a list of var
#global variables at the top
rainbow = [
    '#ff0000',
    '#ff9900',
    '#ffff00',
    '#00ff00',
    '#0099ff',
    '#6633ff'
    ]

strokecolor = rainbow[0]
strokeweight = 3
drawmode = 'free'
strokecap = ROUND


def setup():
    size(600,600)
    background('#004477')
    wendy = createFont('wendy', 20)
    textFont = (wendy)
    
    
def draw():
    global strokecolor, drawmode
    
    strokeCap(strokecap)
    
    #blackpanel
    noStroke()
    fill('#000000')
    rect(0,0,60,height)
    
    #clearbutton
    if mouseX < 60 and mouseY > height-100 and mouseY < height-100+30:
        fill('#ff3399')
        rect(0,height-100,60,30)
        
        if mousePressed:
            background('#004477')
            fill('#000000')
            rect(0,0,60,height)
    
    fill('#ffffff')
    text('clear', 10, height-80)
    
    #colors
    fill(rainbow[0])
    rect(0,0,30,30)
    fill(rainbow[1])
    rect(0,30,30,30)
    fill(rainbow[2])
    rect(0,60,30,30)
    fill(rainbow[3])
    rect(30,0,30,30)
    fill(rainbow[4])
    rect(30,30,30,30)
    fill(rainbow[5])
    rect(30,60,30,30)

    if mousePressed:
        if mouseX < 30:
            if mouseY < 30:
                strokecolor = rainbow[0]
                print('red')
            elif mouseY < 60:
                strokecolor = rainbow[1]
                print('orange')
            elif mouseY < 90:
                strokecolor = rainbow[2]
                print('yellow')
                
        elif mouseX < 60:
            if mouseY < 30:
                strokecolor = rainbow[3]
                print('green')
            elif mouseY < 60:
                strokecolor = rainbow[4]
                print('blue')
            elif mouseY < 90:
                strokecolor = rainbow[5]
                print('purple')
            
    #brushprofile 
    noStroke()
    fill(strokecolor)
    
    if strokecap == ROUND: 
        ellipse(30,123,strokeweight,strokeweight)
    elif strokecap ==SQUARE:
        rect(30-strokeweight/2,123-strokeweight/2,strokeweight,strokeweight)
    
    strokeWeight(strokeweight)
    
    #free-mode
    fill('#ffffff')
    text('-----', 10,165)
    
    if mouseX < 60 and mouseY > 180 and mouseY < 180+30:
        noStroke()
        fill('#ff3399')
        rect(0,170,60,30)
        
        if mousePressed:
            drawmode = 'free'
    
    if drawmode == 'free':
        fill('#ff99ff')
    else:
        fill('#ffffff')
        
    text('free', 10, 190)
    
    #line-mode
    if mouseX < 60 and mouseY > 200 and mouseY < 220+30:
        noStroke()
        fill('#ff3399')
        rect(0,200,60,30)
        
        if mousePressed:
            drawmode = 'line'
        
    if drawmode == 'line':
        fill('#ff99ff')
    else:
        fill('#ffffff')
        
    text('line', 10, 220)
    
    #erase-mode
    if mouseX < 60 and mouseY > 240 and mouseY < 240+30:
        noStroke()
        fill('#ff3399')
        rect(0,230,60,30)
        
        if mousePressed:
            drawmode = 'erase'
    
    if drawmode == 'erase':
        fill('#ff99ff')
        stroke('#004477')
        if mouseButton == LEFT:
            line(mouseX,mouseY,pmouseX,pmouseY)
    else:
        fill('#ffffff')
        stroke(strokecolor)
        
    text('erase', 10, 250)
    
    #ellipse-mode
    if mouseX < 60 and mouseY > 260 and mouseY < 260+30:
        noStroke()
        fill('#ff3399')
        rect(0,260,60,30)
        
        if mousePressed:
            drawmode = 'dots'
        
    if drawmode == 'dots': #won't work with squares
        fill('#ff99ff')
        for i in range(5):
            point(random(width), random(height))
    else:
        fill('#ffffff')
    text('dots', 10, 280)
    
    #draw
    stroke(strokecolor)
    #indication of mouseclick/listen for when the left mouse button has been clicked
    #use print(mouseButton) to find the values or use keycodes
    if mouseButton == LEFT and mouseX > 60 and drawmode == 'free' and 'dots':
        line(mouseX,mouseY,pmouseX, pmouseY) #draw a line between the 1st frame & 2nd frame
        
startx = None
starty = None

def mousePressed(): #get's triggered whenever the mouse is pressed, listens once and then released
    global strokeweight,startx,starty
    
    if mouseButton == LEFT:
        if mouseX > 60:
            startx = mouseX
            starty = mouseY
    
    if mouseButton == RIGHT:
        if strokeweight < 40: 
            strokeweight += 3
        
    if mouseButton == CENTER: 
        strokeweight -= 3

def keyPressed(): #listens to your keyboard
    global strokecap
    if key == '1':
        strokecap = ROUND
    if key == '2':
        strokecap = SQUARE
        
def mouseReleased(): 
    if drawmode == 'line' and startx: 
        line(startx,starty,mouseX,mouseY)
    
