size(800,800)
background("#00000")
fill("#f1b531")
stroke("#d28b17")
strokeWeight(0)
ellipse(400,400,600,600)
strokeWeight(10)


beginShape()
vertex(200,350)
bezierVertex(100,550,700,200,600,400)
endShape()

line(400,375,370,430)
line(370,430,410,420)
line(410,420,370,450)
line(370,450,390,470)
line(390,470,370,520)

saveFrame()
