x=0
dx=5

def setup():
    size(800,600)
    
def draw():
    global x,dx
    fill(0,0,255)
    background(0)
    ellipse(x,height/2,100,100)
    x+=dx
        
    if x>width:
        dx=-5
    if x==0:
        dx=5 
