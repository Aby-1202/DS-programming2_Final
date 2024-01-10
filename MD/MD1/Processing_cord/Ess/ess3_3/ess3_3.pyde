def setup():
    size(800,600)
    x = width/2
    y = height/2
    diameter = 200 #真ん中の円の直径
        
    ellipse(x,y,diameter*2,diameter*2) #大きな円
    ellipse(x,y,diameter,diameter) #真ん中の円
    ellipse(x+100,y,diameter/2,diameter/2) #小さな円1
    ellipse(x-50,y+85,diameter/2,diameter/2) #小さな円2
    ellipse(x-50,y-85,diameter/2,diameter/2) #小さな円3
    
