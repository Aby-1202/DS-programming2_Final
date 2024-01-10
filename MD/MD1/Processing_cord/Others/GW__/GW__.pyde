##setup

size(800,600)
background(255,255,255)
strokeWeight(2)

##make face

fill(231,159,109)
stroke(0,0,0)
ellipse(400,300,550,550)

##make nose

#make red circle
fill(214,69,38)
stroke(0,0,0)
ellipse(400,300,130,130)
#make white square
fill(255,255,255)
stroke(255,255,255)
rect(375,255,45,35)

##make left cheek

#make red circle
fill(214,69,38)
stroke(0,0,0)
ellipse(260,300,150,150)
#make half circle
fill(214,69,38)
stroke(231,159,109)
arc(260,300,150,150,HALF_PI,PI+HALF_PI)
#make white square
fill(255,255,255)
stroke(255,255,255)
rect(270,260,30,25)

##make right cheek

#make red circle
fill(214,69,38)
stroke(0,0,0)
ellipse(540,300,150,150)
#make half circle
fill(214,69,38)
stroke(231,159,109)
arc(540,300,150,150,PI+HALF_PI,TWO_PI+HALF_PI)
#make white square
fill(255,255,255)
stroke(255,255,255)
rect(500,260,30,25)

##make eyes

#make left eye
fill(0,0,0)
stroke(0,0,0)
ellipse(335,180,40,75)
#make right eye
fill(0,0,0)
stroke(0,0,0)
ellipse(465,180,40,75)

##make eyebrows

#make left eyebrow
fill(231,159,109)
stroke(0,0,0)
arc(335,130,80,100,PI,TWO_PI)
#make right eyebrow
fill(231,159,109)
stroke(0,0,0)
arc(470,130,80,100,PI,TWO_PI)

##make mouth

#make mouth
fill(137,63,72)
stroke(0,0,0)
arc(400,372,230,260,TWO_PI,TWO_PI+PI)
#make under the nose
fill(231,159,109)
stroke(0,0,0)
arc(400,372,230,50,TWO_PI,TWO_PI+PI)
