import time    
import threading

def watch_tv(x):
    if not exists("1457840008261.png"):   
        click("1457839907867.png")
    click("1457839943697.png")
    time.sleep(x)
    if not exists("1457840267405.png"):
        click("1457840693591.png")
    click("1457840267405.png")
    click("1457840775610.png")
def chests():
    c=0
    if exists("1458015332851.png"):
        c=5
        click("1458015409623.png")
    if exists("1457885255132.png"):
        c=6
        click("1458015409623.png")
    time.sleep(1)
    for i in range(0,c):
        click("1457885268951.png")
    if exists("1457885139771.png"):
        click("1457885139771.png")
        click("1458015477129.png")
    for i in range(0,2):
        if exists("1457885556109.png"):
             click("1457885556109.png")
             time.sleep(1)
             for i in range(0,4):
                  click("1457885268951.png")
#watch_tv(10)
#click("1458104067967.png")
#click("1458104105051.png")
#time.sleep(0.5)
#type("lol dis is vlad bot")
#click("1458187324243.png")
#click("1458187357146.png")

while True:
    time.sleep(3)
    click("1458143926796.png")
    chests()