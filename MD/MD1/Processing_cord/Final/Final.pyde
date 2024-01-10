def setup():
    global num, a, x, y, font, Box_ON, Box_OFF, scene, lines
    size(1200,800)
    frameRate(60)
    font = createFont(u'MSゴシック',50)
    num = 20
    x = [0]*num
    y = [0]*num
    lines = loadStrings("planet.csv")
    scene = "Menu_mode"
            
    def Box_ON(): #カーソルが重なっている時の色を設定
        stroke(255)
        fill(199)
        
    def Box_OFF(): #通常時の色を設定
        stroke(255)
        fill(0)
        
def menu():
    global num, a, x, y
    background(0)
    img = loadImage("img.png")
    image(img,0,0,1200,800)
    textFont(font)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
            
    if 50 <= x[a] <= 215 and 20 <= y[a] <= 100: #太陽のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(50,20,165,80)
    fill(255)
    text(u"太陽",85,80)
    if 50 <= x[a] <= 215 and 170 <= y[a] <= 250: #水星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(50,170,165,80)
    fill(255)
    text(u"水星",85,230)
    if 50 <= x[a] <= 215 and 320 <= y[a] <= 400: #金星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(50,320,165,80)
    fill(255)
    text(u"金星",85,380)
    if 50 <= x[a] <= 215 and 470 <= y[a] <= 530: #地球のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(50,470,165,80)
    fill(255)
    text(u"地球",85,530)
    if 50 <= x[a] <= 215 and 620 <= y[a] <=700: #火星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(50,620,165,80)
    fill(255)
    text(u"火星",85,680)
    if 270 <= x[a] <= 440 and 20 <= y[a] <= 100: #木星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(275,20,165,80)
    fill(255)
    text(u"木星",310,80)
    if 270 <= x[a] <= 440 and 170 <= y[a] <= 250: #土星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(275,170,165,80)
    fill(255)
    text(u"土星",310,230)
    if 270 <= x[a] <= 440 and 320 <= y[a] <= 400: #天王星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(275,320,165,80)
    fill(255)
    text(u"天王星",285,380)
    if 270 <= x[a] <= 440 and 470 <= y[a] <= 530: #海王星のボタンの色を変える
        Box_ON()
    else:
        Box_OFF()
    rect(275,470,165,80)
    fill(255)
    text(u"海王星",285,530)
    fill(255,255,0)
    textSize(120)
    text(u"太陽系惑星", 490, 580)
    text(u"データリスト", 530, 750)
    
def sun():
    global num, a, x, y
    background(0)
    img_sun = loadImage("sun.png")
    image(img_sun,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    sun_r = (lines[1].split(',')[1])
    sun_w = (lines[1].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(sun_r,800,300)
    text(u'[公転周期]',800,500)
    text(sun_w,800,650)
    
def mercury():
    global num, a, x, y
    background(0)
    img_mercury = loadImage("mercury.png")
    image(img_mercury,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    mercury_r = (lines[2].split(',')[1])
    mercury_w = (lines[2].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(mercury_r,800,300)
    text(u'[公転周期]',800,500)
    text(mercury_w,800,650)
    
def venus():
    global num, a, x, y
    background(0)
    img_venus = loadImage("venus.png")
    image(img_venus,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    venus_r = (lines[3].split(',')[1])
    venus_w = (lines[3].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(venus_r,800,300)
    text(u'[公転周期]',800,500)
    text(venus_w,800,650)
        
def earth():
    global num, a, x, y
    background(0)
    img_earth = loadImage("earth.png")
    image(img_earth,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    earth_r = (lines[4].split(',')[1])
    earth_w = (lines[4].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(earth_r,800,300)
    text(u'[公転周期]',800,500)
    text(earth_w,800,650)

def mars():
    global num, a, x, y
    background(0)
    img_mars = loadImage("mars.png")
    image(img_mars,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    mars_r = (lines[5].split(',')[1])
    mars_w = (lines[5].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(mars_r,800,300)
    text(u'[公転周期]',800,500)
    text(mars_w,800,650)

def jupiter():
    global num, a, x, y
    background(0)
    img_jupiter = loadImage("jupiter.png")
    image(img_jupiter,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    jupiter_r = (lines[6].split(',')[1])
    jupiter_w = (lines[6].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(jupiter_r,800,300)
    text(u'[公転周期]',800,500)
    text(jupiter_w,800,650)
    
def saturn():
    global num, a, x, y
    background(0)
    img_saturn = loadImage("saturn.png")
    image(img_saturn,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    saturn_r = (lines[7].split(',')[1])
    saturn_w = (lines[7].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(saturn_r,800,300)
    text(u'[公転周期]',800,500)
    text(saturn_w,800,650)

def uranus():
    global num, a, x, y
    background(0)
    img_uranus = loadImage("uranus.png")
    image(img_uranus,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    uranus_r = (lines[8].split(',')[1])
    uranus_w = (lines[8].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(uranus_r,800,300)
    text(u'[公転周期]',800,500)
    text(uranus_w,800,650)

def neptune():
    global num, a, x, y
    background(0)
    img_neptune = loadImage("neptune.png")
    image(img_neptune,0,0,700,800)
    for a in range(num-1, 0, -1):
        x[a] = x[a-1]
        y[a] = y[a-1]
            
    x[0] = mouseX
    y[0] = mouseY
    neptune_r = (lines[9].split(',')[1])
    neptune_w = (lines[9].split(',')[2])
    textSize(50)
    text(u'[半径]',800,150)
    text(neptune_r,800,300)
    text(u'[公転周期]',800,500)
    text(neptune_w,778,650)
    
def sceneSet(): #シーンを設定
    global a, x, y, scene
    if scene == "Menu_mode":
        menu()
    if scene == "Sun_mode":
        sun()
    if scene == "Mercury_mode":
        mercury()
    if scene == "Venus_mode":
        venus()
    if scene == "Earth_mode":
        earth()
    if scene == "Mars_mode":
        mars()
    if scene == "Jupiter_mode":
        jupiter()
    if scene == "Saturn_mode":
        saturn()
    if scene == "Uranus_mode":
        uranus()
    if scene == "Neptune_mode":
        neptune()
        
    if mousePressed: #ボタンを押した際に行われる画面遷移を設定
        if 50 <= x[a] <= 215 and 20 <= y[a] <= 100: #太陽のボタン
            scene = "Sun_mode"
        elif 50 <= x[a] <= 215 and 170 <= y[a] <= 250: #水星のボタン
            scene = "Mercury_mode"
        elif 50 <= x[a] <= 215 and 320 <= y[a] <= 400: #金星のボタン
            scene = "Venus_mode"
        elif 50 <= x[a] <= 215 and 470 <= y[a] <= 530: #地球のボタン
            scene = "Earth_mode"
        elif 50 <= x[a] <= 215 and 620 <= y[a] <=700: #火星のボタン
            scene = "Mars_mode"
        elif 245 <= x[a] <= 410 and 20 <= y[a] <= 100: #木星のボタン
            scene = "Jupiter_mode"
        elif 245 <= x[a] <= 410 and 170 <= y[a] <= 250: #土星のボタン
            scene = "Saturn_mode"
        elif 245 <= x[a] <= 410 and 320 <= y[a] <= 400: #天王星のボタン
            scene = "Uranus_mode"
        elif 245 <= x[a] <= 410 and 470 <= y[a] <= 530: #海王星のボタン
            scene = "Neptune_mode"
    textSize(100)
    if scene != "Menu_mode" and 1040 <= x[a] <= 1170 and 20 <= y[a] <= 100:
        Box_ON()
        rect(1040,20,130,80)
        fill(255)
        text(u"↩",1055,105)
    elif scene != "Menu_mode":
        Box_OFF()
        rect(1040,20,130,80)
        fill(255)
        text(u"↩",1055,105)
    if mousePressed:
        if 1040 <= x[a] <= 1170 and 20 <= y[a] <= 100: #ボタンを押すとメニューに戻る
            scene = "Menu_mode"
            
def draw():
    sceneSet()
