size(600,600)

noFill()

for i in range(20):
    curve(0,600,0,200 + i * 10,600,200 + i * 10,300,0)
    curve(0,200,0,200 + i * 10,600,200 + i * 10,300,500)

saveFrame('pattern.tif')
