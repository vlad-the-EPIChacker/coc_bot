import time
from random import randint

def ratioclk(x, y, c):
    click(c)
    scrn=Screen()
    res=scrn.getBounds()
    x1, y1= (res.width*x, res.height*y)
    pointA = Location(x1, y1)   
    click(pointA)


def attack():
    click("1463358584540.png")
    state='defense'
    time.sleep(1)
    attack=["1463358928623.png","1463358738718.png","1463358762423.png"]
    defense=["1463358716044.png","1463358731931.png","1463362472398.png"]
    
    spell=["1463358725056.png","1463358772273.png"]
    deck=spell+defense+attack
    towers=[(0.45,0.25), (0.5, 0.15)]
    while not exists("1463358584540.png"):
        clked=0
        for c in deck:
            if exists(c):
                try:
                    #time.sleep(0.5)
                    if c in spell:
                        ran=towers[randint(0, 2)]
                        ratioclk(ran[0], ran[1], c)
                        clked=1
                        print 'spell1'
                    else:
                        if state== 'defense' and c in defense:
                            state='attack'
                            ratioclk(0.4,0.55, c)
                            clked=1
                            print 'defense'
                        elif state== 'attack' and c in attack:
                            state='defense'
                            ratioclk(0.4,0.55, c)
                            clked=1
                            print 'attack'
                except:
                    print "Unexpected error:", sys.exc_info()[0]
            if clked==0:
                for c in deck:
                    if exists(c):
                        
                        try:
                            #time.sleep(0.5)
                            if c in spell:
                                ran=towers[randint(0, 2)]
                                ratioclk(ran[0], ran[1], c)
                                print 'spell2'
                            else:
                                ratioclk(0.4,0.55, c)
                                print 'random'
                        except:
                            print "Unexpected error:", sys.exc_info()[0]

attack()
