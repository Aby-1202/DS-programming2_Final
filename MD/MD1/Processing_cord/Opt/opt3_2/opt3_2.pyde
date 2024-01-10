def setup():
    global num, x,y
    size(800,600)
    frameRate(60)
    num = 60
    x = [0] * num
    y = [0] * num
    
def draw():
    global num,x,y
    background(192)
    
    for i in range(num - 1, 0, -1):
        x[i] = x[i - 1]
        y[i] = y[i - 1]
        
    x[0] = mouseX
    y[0] = mouseY
    
    for i in range(num):
       fill(i*3.2)
       rect(x[i], y[i], 50, 100)
