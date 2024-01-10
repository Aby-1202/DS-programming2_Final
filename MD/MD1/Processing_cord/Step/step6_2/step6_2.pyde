add_library('Minim')

amp = 400.0 # Soundファイルから入力された信号の増幅率を設定

def setup():
    # グローバル変数
    global minim, player
        
    size(800,200)
    
    # Minimのインスタンスを生成
    minim = Minim(this)
    player = minim.loadFile('../../sounddata/marcus_kellis_theme.mp3')
    player.loop()
    
    # 線の太さ、色を設定
    strokeWeight(2)
    stroke(0, 255, 0)
        
    
def draw():
    # グローバル変数
    global player
    
    # ウィンドウの背景色を黒に設定（線が残らないように塗り替える）
    background(0)
        
    for i in range(1, player.bufferSize()):
        current_volume = player.left.get(i)
        previous_volume = player.left.get(i-1)
        line(i-1, previous_volume*amp, i,current_volume*amp)
