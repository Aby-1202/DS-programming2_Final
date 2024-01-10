loc_x = []
loc_y = []
season = []
number = 0

play_year = [
         '1996','1997','1998','1999', '2000','2001','2002','2003', '2004','2005','2006','2007',
         '2008','2009','2010','2011', '2012','2013','2014','2015', '2016'
        ]

def setup():
    global loc_x, loc_y, season, number
    size(600,600)
    textSize(64)
    background(0)
    frameRate(3)
    read_csv()
    
def draw():
    global loc_x, loc_y, season, number, play_year
    background(0)
    
    fill((float)(number)/len(play_year)*255,200,200,200)
    for i in range(len(loc_x)):
        if(play_year[number] in season[i]):
            ellipse((int)(loc_x[i])+width/2,(int)(loc_y[i]),10,10)
    
    fill(255)
    text(play_year[number],width/2,height/2+100)
    
    if number < len(play_year)-1:
        number += 1
    else:
        number = 0
    
def read_csv():
    global loc_x, loc_y, season
    lines = loadStrings("kobe_shot_cleaned.csv")
    for i in range(1, len(lines)):
        for j, data in enumerate(lines[i].split(',')):
            if j == 0:
                loc_x.append(data)
            if j == 1:
                loc_y.append(data)
            if j == 6:
                season.append(data)
