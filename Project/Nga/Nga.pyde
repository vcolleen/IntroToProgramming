size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)

beginShape()
vertex(220,250)
bezierVertex(200,270,200,290,220,300)
vertex(220,300)
bezierVertex(420,400,420,400,220,500)
vertex(220,500)
bezierVertex(200,510,200,550,220,550)
endShape()

beginShape()
line(370,400,390,402)
vertex(390,400)
bezierVertex(420,440,420,440,420,400)
vertex(420,400)
bezierVertex(400,280,520,280,560,320)
vertex(560,320)
bezierVertex(640,400,640,440,520,600)
endShape()

saveFrame()
