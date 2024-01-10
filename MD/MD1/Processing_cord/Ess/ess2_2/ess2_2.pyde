size(800,600)

x=50
d=30
for i in range(15):
    if i>7:
        fill(0,0,255)
    elif i==7:
        fill(0,255,0)
    else:
        fill(255,0,0)

    ellipse(x+i*50,height/2,d,d)
