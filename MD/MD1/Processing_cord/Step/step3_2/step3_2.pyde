def setup():
    size(800,600)
    
def draw():
    pass
    
def mousePressed():
    if mouseButton == LEFT:
        draw_car()
    
def draw_car():
    x = mouseX
    y = mouseY
    fill (0, 255, 255)
    rect(x-25, y-25, 50, 25)
    fill(255,200,0)
    rect(x-50, y,100, 25)
    fill(60)
    ellipse(x-25, y+25, 25, 25)
    ellipse(x+25, y+25, 25, 25)
