size(800,800)
grid = loadImage('grid.png')
beziers = loadImage('beziers.png') 
image(grid,0,0)
image(beziers,0,0)
noFill()
stroke('#ffffff')
strokeWeight(3)

#curve 1 
beginShape()
vertex(182, 115)
bezierVertex(110,220,330,250,270,325)
endShape()

#curve 2
beginShape()
vertex(260,460)
bezierVertex(230,750,90,480,320,580)
endShape()

#curve3
beginShape()
vertex(460,120)
bezierVertex(450,280,690,285,640,120)
endShape()

#curve4
beginShape()
vertex(490,620)
bezierVertex(580,730,710,630,600,530) 
endShape()
