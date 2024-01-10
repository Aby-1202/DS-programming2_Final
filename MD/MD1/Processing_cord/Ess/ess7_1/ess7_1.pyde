def setup():
    global angle
    size(400, 400, P3D)
    frameRate(10)
    angle = 0 # 角度を設定するための変数
 
def draw():
    global  angle
    background(0)
    directionalLight(0, 255, 0, 0,0.5,-1) # 緑の環境光   
    translate(width/2, height/2) # 立体の中心を画面中央に移動 
    rotateX(radians(-30))              # X軸に対して30°だけ回転
    rotateY(radians(angle))                     # Y軸に対してangleの数値分だけ回転
    box(150)                  # 150pxの立方体を描く
    
    angle += 0.5             # 角度を0.5ずつ足していく    変数名 += 値
    if angle > 360.0: 
       angle = 0.0      # 360度を超えたら0に戻す    
