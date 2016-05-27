import time
from random import randint

g_cregoin=Region(750,980,536,217)
g_kregion=Region(873,1018,174,84)


def fIA(image, region):
    aMatch = region.exists(image)
    if aMatch==None:
        return (False, None)
    else:
        return (True, aMatch)


def ratioclk(x, y, c):
    time.sleep(2)
    click(c)
    scrn=Screen()
    res=scrn.getBounds()
    x1, y1= (res.width*x, res.height*y)
    pointA = Location(x1, y1)   
    click(pointA)


def attack():
    click("1463358584540.png")
    if exists("1464103076997.png"):
        click("1464103076997.png")
    state=0
    time.sleep(1)
    attack=["1463358928623.png","1463358738718.png","1463358762423.png"]
    defense=["1463358716044.png","1463358731931.png","1463362472398.png"]
    
    spell=["1463358725056.png","1463358772273.png"]
    deck=spell+defense+attack
    towers=[(0.45,0.25), (0.5, 0.15)]
    state=randint(0,1)
    while not fIA("1464062086927.png", g_kregion)[0]:
        clked=0
        for c in deck:
            try:       
                u=fIA(c, g_cregoin)
                if u[0]:
                    #time.sleep(0.5)
                    if c not in spell:
                        if state==0:
                            ratioclk(0.4,0.55, u[1])
                        else:
                            ratioclk(0.6,0.55, u[1])
                    else:
                        ran=towers[1]
                        ratioclk(ran[0], ran[1], u[1])
                        clked=1
                        print 'spell1'
            except:
                print "Unexpected error:", sys.exc_info()[0]
    click("1464062086927.png")
while True:
    attack()