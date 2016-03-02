import time
myScriptPath = "C:\\Users\\vlad\\Desktop\\Projects sirkulix"
if not myScriptPath in sys.path: sys.path.append(myScriptPath)
import pics
reload(pics)
def chat(msg):
    if not exists(pics.pics["chatbar"]):
        click(pics.pics["chat1"])        

    wait(pics.pics["chatbar"])
    click(pics.pics["chatbar"])
    wait(pics.pics["chatbar2"])
    type(msg)
    click(pics.pics["send"])
def collect():
    click(pics.pics["elixer_c"])
    if exists(pics.pics["elixir1"]):
        click(pics.pics["elixir1"])
    else:
        return

chat("hello world")
#collect()