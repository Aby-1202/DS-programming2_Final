x=0
y=0
d=57.3
dx=0.00025
dy=0.00025

def setup():
    size(800,800)
    noStroke()
    
    def draw():
        global x,y,dx,dy
        background(0)
        for i in range(20):
            for j in range(20):
                if 0+40*i+x*i>=600:
                    noFill()
                elif 0*40*j+y*j>=600:
                    noFill()
                else:
                    fill(255)
                ellipse(0+40*i+x*i,0+40*j+y*j,d-i-h*i,0+40*j+y*j,d-i-h*i)
                
                x += dx
                y += dy
                d += dy/10
