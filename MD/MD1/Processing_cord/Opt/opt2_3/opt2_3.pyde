x=400
y=0
d=40
dx=0.3

def setup():
    size(800,800)

def draw():
    global x,y,d,dx
    background(0)
    for i in range(20):
        fill(54+i*8.85,123+i*1/2,246-i*3/4)
        ellipse(x+sin(1+i*0.8)*200,y+i*d,d,d)
        
        if x >= width or x <= 0:
            dx *= -1
