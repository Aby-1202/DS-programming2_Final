def setup():
    size(800,600)
    background(192)
    noStroke()
    num = 1
    global num,x,y
    x = [0]*num
    y = [0]*num
    
def draw():
    global num,x,y
    x[0] = mouseX
    y[0] = mouseY
    for i in range(20):
        for j in range(20):
            fill(255)
            dist = (mouseX, mouseY, 0+40*i, 0+40*j)
            ball_size = ()
            ellipse(0+40*i,0+40*j,56,56)
