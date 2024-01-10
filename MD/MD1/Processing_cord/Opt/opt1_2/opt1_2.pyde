size(800,800)
background(0)

for i in range(20):
    for j in range(20):
        noStroke()
        fill(255)
        ellipse(0+40*i,0+40*j,56-i-j*9/5,56-i-j*9/5)
        ellipse(0+40*j,0+40*i,56-i-j*9/5,56-i-j*9/5)        
