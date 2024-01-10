def setup():
    global data, num
    size(800,600)
    lines = loadStrings("y-line.csv")
    data = []
    num = 0
    
    for i in range(1,len(lines)):
        data.append(float(lines[i].split(',')[1]))
        
def draw():
    global data, num
    background(192)
    ellipse(width/2, height/2-20*data[num], 100, 100)
    num += 1
    if(len(data)<=num):
        num = 0            
