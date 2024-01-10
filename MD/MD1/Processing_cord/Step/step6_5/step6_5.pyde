add_library('minim')
amp = 100
def setup() :
    size(1024,600)
    background(0)

    global player
    minim = Minim(this)
    player = minim.loadFile("../../sounddata/sample.mp3")
    player.loop()
    
    # 周波数解析
    global fft
    fft = FFT(player.bufferSize(), player.sampleRate()/2)
    fft.window(FFT.HAMMING) #窓関数
    
def draw() :
    global player, fft
    background(0)
    stroke(255)
# つづき
    # 描画
    for i in range(1, fft.specSize()) :
        x = map(i, 0, fft.specSize(), 0, width)
        line(x, height, x, height - fft.getBand(i) * amp)

def stop():
    player.close()
    minim.stop()
