def setup():
    size(600,600)
    background('#004477')
    frameRate(12)

def draw():
    print(mouseX) 
    print(mouseY)
    
    fill(0x77004477) #Use 0&x so you dont have to put a hashtag - (77) is transparency
    rect(0,0,width,height)
    
    fill('#ffffff')
    ellipse(mouseX,mouseY,10,10) 
