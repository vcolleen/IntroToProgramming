size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)


beginShape()
vertex(300,300)
bezierVertex(380,210,500,260,390,350)
vertex(390,350)
bezierVertex(570,500,190,600,180,460)
endShape()

beginShape()
vertex(432,300)
bezierVertex(650,200,450,700,650,450)
endShape()

saveFrame()
