size(800,800)
grid = loadImage('grid.png')
image(grid, 0,0)
noFill()
stroke('#ffffff') #white-line
strokeWeight(3)

fill('#6633ff') #purple-fill

#square top-left
beginShape()
vertex(100,100)
vertex(200,100)
vertex(200,200)
vertex(100,200)
endShape(CLOSE) #add the close function to automatically finish the shape

#curve in the middle
noFill()
beginShape() #whenever you use curves, always have to start with a vertex
vertex(400,200)
bezierVertex(
    300,300,
    500,500,
    400,600 
)
endShape()

#heart 
fill('#ff0000')
beginShape()
vertex(600,400)
bezierVertex(
    420,300,
    550,150,
    600,250,
) 
bezierVertex(
    650,150,
    780,300,
    600,400
)
endShape()

#coin
#if you want to take out a shape in another shape, go the opposite direction of the initial shape 
fill('#00ff00')
beginShape()
vertex(100,600)
bezierVertex(
    100,545,
    145,500,
    200,500,
)
bezierVertex(
    255,500,
    300,545,
    300,600,
)
bezierVertex(
    300,655,
    255,700,
    200,700,
)
bezierVertex(
    145,700,
    100,655,
    100,600,
)
beginContour() #how to take out a shape, in a shape 
vertex(180,580)
vertex(180,620)
vertex(220,620)
vertex(220,580)
endContour()
endShape()
