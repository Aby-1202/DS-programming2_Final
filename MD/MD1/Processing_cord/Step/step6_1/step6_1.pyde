add_library('minim')
def setup():
    # グローバル変数
    global minim, player
    minim =  Minim(this)
    player = minim.loadFile('../sounddata/sample.mp3',735)
    player.play()
    #player.loop() #ループさせたいときはこちらで再生
def draw():
    pass  
def stop():
    player.close()
    minim.stop()
