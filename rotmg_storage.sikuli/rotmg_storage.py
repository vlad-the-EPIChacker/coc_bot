import time

def hi():
    click("1463804164417.png")
    time.sleep(0.5)
    type(Key.ENTER)
    type('hi')
    type(Key.ENTER)

def deposit():
    click(username)
    click("1463805572750.png")
    time.sleep(6)
    click("1463805668630.png")
    time.sleep(5)
    if exists("1463805738841.png"):
        click("1463805738841.png")

commands={}
commands["1463804433818.png"]=hi
commands["1463806539371.png"]=deposit
username="1463803318693.png"

while True:
    if exists("1463803274995.png") and exists(username):
        for i in commands.keys():
            if exists(i):
            commands[i]()