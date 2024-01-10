def setup():
    size(800,600)
    for i in range(10):
        draw_car()
    
def draw_car():
    x = int(random(800))
    y = int(random(600))
    fill (0, 255, 255)
    rect(x-25, y-25, 50, 25)
    fill(255,200,0)
    rect(x-50, y,100, 25)
    fill(60)
    ellipse(x-25, y+25, 25, 25)
    ellipse(x+25, y+25, 25, 25)
