size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)


beginShape()
vertex(200,300)
bezierVertex(100,500,700,150,600,350)
endShape()

beginShape()
vertex(200,500)
bezierVertex(100,700,700,350,600,550)
endShape()

saveFrame()

line(400,325,400,525)
