import time

def ratioclk(x, y):
    scrn=Screen()
    res=scrn.getBounds()
    x1, y1= (res.width*x, res.height*y)
    pointA = Location(x1, y1)   
    click(pointA)


def attack():
    click("1463358584540.png")
    time.sleep(1)
    deck=["1463358928623.png","1463358716044.png","1463358725056.png","1463358731931.png","1463358738718.png","1463358762423.png","1463358772273.png"]
    while not exists("1463358584540.png"):
        time.sleep(0.5)
        for c in deck:
            if exists(c):
                try:
                    click(c)
                    ratioclk(0.4,0.55)
                except:
                    print "Unexpected error:", sys.exc_info()[0]


attack()
