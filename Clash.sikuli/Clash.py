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
    ne=list([x for x in findAll(pics.pics["elixir_c"])])
    for i in range(0, len(ne)):
        click(ne[i])
        if exists(pics.pics["elixir1"]):
            click(pics.pics["elixir1"])
    ne=list([x for x in findAll(pics.pics["gold_m"])])
    for i in range(0, len(ne)):
        click(ne[i])
        if exists(pics.pics["gold1"]):
            click(pics.pics["gold1"])  

def parse(x):
    y=0
    try:
        y=int(x)
    except:
        y=x.replace("I","1")
        y=y.replace("Z","2")
    return int(y)
def train_troops():
    click(pics.pics["barracks"])
    click(pics.pics["train"])
    x=find(pics.pics["troop_c"]).text()
    z=find(pics.pics["train_c"]).text()
    print z
    full=z.split("/")
    print full
    troops=x.split("/")
#    print troops
    troops[0]=parse(troops[0])
    troops[1]=parse(troops[1])
    full[0]=parse(full[0])
    full[1]=parse(full[1])
    time.sleep(1)
    while troops[0]<troops[1]:
        if full[0]>full[1]:
            if exists(pics.pics["switch"]):
                click(pics.pics["switch"])
        troops[0]=troops[0]+1
        full[0]=full[0]+1
        click(pics.pics["barb"])

#chat("hello world")
while True:
    collect()
#train_troops()