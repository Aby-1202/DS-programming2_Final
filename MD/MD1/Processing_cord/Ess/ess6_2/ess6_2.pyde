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
  background(0);

def keyPressed():
    if key == '1':
        wave.setFreq(440.00)
  
    if key == '2':
        wave.setFreq(493.883)

    if key == '3':
        wave.setFreq(523.251)
        
    if key == '4':
        wave.setFreq(587.330)
        
    if key == '5':
        wave.setFreq(659.255)
        
    if key == '6':
        wave.setFreq(698.456)
    
    if key == '7':
        wave.setFreq(783.989)
        
    if key == '8':
        wave.setFreq(880.000)
    
def keyReleased():
    global wave
    wave.setFreq(0)

def stop():
    out.close()
    minim.stop()
