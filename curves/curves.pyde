size(500,500)
grid = loadImage('grid.png') #how to put an image in via variable
image(grid, 0, 0)
noFill()
strokeWeight(3)

stroke('#0099ff') #blue-line
#line(100,100,400,400)
curve(0, 0, 100,100,400,400,500,500)

curveTightness(0) #CurveTightness(0) is the default, should go from -5 to 5 
stroke('#ffff00') #yellow-line
curve(0, 250, 100,100,400,400,500,250)

stroke('#FF9900') #orange-line 
curve(0, 250, 0, 250, 100, 100, 400, 400)
curve(100, 100, 400, 400, 500, 250, 500, 250)

#beziercurve - takes 6 arguments 
stroke('#ff99ff') #pink-line
cp1x = 100 #just a variable, it's named cp1x in short of control pont 1 x position, used to visualize where the lines are 
cp1y = 50
cp2x = 400
cp2y = 450
bezier(
    400, 100,
    cp1x, cp1y,
    cp2x, cp2y, 
    100, 400
)

stroke('#FF0000') #red-line, showing the anchors of what we're bending 
line(400, 100, cp1x, cp1y)
line(100, 400, cp2x, cp2y);
