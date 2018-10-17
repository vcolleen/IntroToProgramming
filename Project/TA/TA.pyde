size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)

beginShape()
vertex(300,350)
bezierVertex(250,350,250,450,320,420)
endShape()

beginShape()
vertex(300,560)
bezierVertex(200,350,700,250,600,350)
endShape()

saveFrame()
