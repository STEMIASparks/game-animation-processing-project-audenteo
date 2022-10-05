D= 65

x1= 65
y1= 550

x2= 165
y2= 650

x3= 265
y3= 750

x4= 365
y4= 850

def setup():
    size (500,500)
    
def draw():
    global x1, y1, x2, y2, x3, y3, x4, y4
     
    #for the four grey boxes up top               
    square(75,50,65)
    fill(102,102,102)
    background(0, 0 ,0)
    #image(loadImage("broccoli-florets.jpg"),0 ,0 , 500, 500)
    #tint(100)
    i = 65
    while i < 425:
        square(i, 20, 65)
        i = i+100
        
    fill(136, 255, 55)
    square(x1, y1, D)
    if y1 <= 1000:
        y1= y1-5
    if y1 == -65:
        y1= 550
    
    fill(136, 255, 55)
    square(x2, y2, D)
    if y2 <= 1000:
        y2= y2-5
    if y2 == -65:
        y2= 650
        
    fill(136, 255, 55)
    square(x3, y3, D)
    if y3 <= 1000:
        y3= y3-5
    if y3 == -65:
        y3= 750
        
    fill(136, 255, 55)
    square(x4, y4, D)
    if y4 <= 1000:
        y4= y4-5
    if y4 == -65:
        y4= 850
def keyPressed():
    global y1, y2, y3, y4
    if y1 < 85 and y1 > 20:
        y1=500
    if y2 < 85 and y2 > 20:
        y2=500
    if y3 < 85 and y3 > 20:
        y3=500
    if y4 < 85 and y4 > 20:
        y4=500
        #print("true")
