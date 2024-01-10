def setup():
   global angle
   size(800, 400, P3D)
   frameRate(60)
   noStroke()
   angle = 70 # 角度を設定するための変数
def draw():
   global  angle
   background(0)
   directionalLight(255,255,255, -1, 0, -1)
   fill(0,104,183)
   pushMatrix()
   translate(width/2, height/2) # 立体の中心を画面中央に移動
   rotateY(radians(angle)) #Y軸に対してangleの数値分だけ回転
   sphere(100)
   popMatrix()
   translate(width/2, height/2)
   fill(255)
   pushMatrix()
   translate(150 * sin(angle),   0, 150 * cos(angle)) # 立体の中心を画面中央に移動
   sphere(10)
   popMatrix()
   angle += 0.05
   rotateY(radians(angle))
   if angle > 360.0: 
       angle = 0.0
