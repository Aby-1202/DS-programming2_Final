x=0
y=100
dx=10
dy=10

def setup():
    size(800,600)
    
def draw():
    global x,dx,y,dy
    fill(129,192,59)
    background(0)
    ellipse(x,y,30,30)
    x+=dx
    y+=dy
    
    if x > width or x == 0:
        dx *= -1
    if y > height or y == 0:
        dy *= -1
