add_library('minim')
def setup():
    # グローバル変数
    global minim, player
    
    textSize(100)
    textAlign(CENTER,CENTER)
    background(0)
    
    size(800,600)
    minim =  Minim(this)
    player = minim.loadFile('../../sounddata/sample.mp3')
    player.play()
    text("Playing" , width/2, height/2)

def draw():
    pass  
def stop():
    player.close()
    minim.stop()
def mousePressed() :
    # マウスで再生オン/オフ
    if player.isPlaying() == True:
        player.pause()
        background(0)
        text("Pause" , width/2, height/2)
    else:
        player.play()
        background(0)
        text("Playing" , width/2, height/2)
