size(800,600)

x=100
y=200
d=100
for i in range(5):
    if 500>x+i*100>300:
        fill(255,0,0)
    else:
        fill(255,255,255)
    ellipse(x+i*100,y,d,d)
