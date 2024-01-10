add_library('minim')

def setup() :
    global minim
    global wave
    
    size(800, 600)
    background(0)

    minim = Minim(this)
    out = minim.getLineOut(Minim.STEREO)
    wave = SineWave(0, 1.0, out.sampleRate())
    out.addSignal(wave)
    
def draw():
    background(0)
def keyPressed():
    if key == '1':
        wave.setFreq(440.00)
  
    if key == '2':
        wave.setFreq(493.88)

    if key == '3':
        wave.setFreq(523.25)
    
def keyReleased():
    global wave
    wave.setFreq(0)

def stop():
    out.close()
    minim.stop()
