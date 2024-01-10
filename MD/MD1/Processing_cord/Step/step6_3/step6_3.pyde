def setup():
    global x, A, T, y1
    size(800,600)
    x = 0
    A = 100
    T = 100
    y1 = height/2
    
def draw():
    global x, A, T
    y = A * sin(TWO_PI * x / T) + y1
    ellipse(x, y, 5, 5)
    x = x + 1
