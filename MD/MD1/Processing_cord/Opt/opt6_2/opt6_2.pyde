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
    wave.setFreq(440×2^(0/12))

if key == '2':
    wave.setFreq(440×2^(2/12))

if key == '3':
    wave.setFreq(440×2^(3/12))
    
if key == '4':
    wave.setFreq(440×2^(5/12))
    
if key == '5':
    wave.setFreq(440×2^(7/12))
    
if key == '6':
    wave.setFreq(440×2^(8/12))

if key == '7':
    wave.setFreq(440×2^(10/12))
    
if key == '8':
    wave.setFreq(440×2^(12/12))
    
def keyReleased():
    global wave
    wave.setFreq(0)

def stop():
    out.close()
    minim.stop()
