size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)


line(200,300,220,390)

beginShape()
vertex(220,390)
bezierVertex(250,420,700,200,600,400)
endShape()

beginShape()
vertex(221,390)
bezierVertex(100,750,700,300,600,500)
endShape()

saveFrame()
