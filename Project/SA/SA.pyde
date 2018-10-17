size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)

line(200,270,260,270)
line(250,270,350,550)
line(350,550,480,300)

beginShape()
vertex(480,300)
bezierVertex(520,220,640,270,530,360)
endShape()

beginShape()
vertex(530,360)
bezierVertex(710,400,350,640,400,560)
endShape()

saveFrame()
