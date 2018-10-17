size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)

strokeWeight(10)
beginShape()
vertex(250,250)
bezierVertex(400,190,250,550,320,550)
vertex(320,550)
bezierVertex(450,550,500,250,600,400)
endShape()

line(225,430,420,320)
line(225,500,420,390)

saveFrame()
