size(800,800)
background(0)

x=400
y=0
d=40
for i in range(20):
    fill(54+i*8.85,123+i*1/2,246-i*3/4)
    ellipse(x+sin(0.44*i)*200,0+i*d,d,d) 
