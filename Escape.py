def game_over():
    for z in range(3):
        rec=Rectangle(Point(int(WIDTH/4),int(HEIGHT/4)),Point(int(3*WIDTH/4),int(3*HEIGHT/4)))
        rec.setFill('blue')
        rec.draw(win)
        txt=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"GAME OVER")
        txt.setTextColor('white')
        txt.setSize(30)
        txt.setStyle('bold')
        txt.draw(win)
        time.sleep(1)
        rec.undraw()
        txt.undraw()
        time.sleep(1)
    win.close()

def winner():
    for z in range(3):
        rec=Rectangle(Point(int(WIDTH/4),int(HEIGHT/4)),Point(int(3*WIDTH/4),int(3*HEIGHT/4)))
        rec.setFill('green')
        rec.draw(win)
        txt=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"YOU WIN")
        txt.setTextColor('white')
        txt.setSize(30)
        txt.setStyle('bold')
        txt.draw(win)
        time.sleep(1)
        rec.undraw()
        txt.undraw()
        time.sleep(1)
    win.close()
from graphics import *
import random
WIDTH,HEIGHT=600,600
win=GraphWin("Escape the guards",WIDTH,HEIGHT)
win.setBackground('black')
GUARD_MOVE=4
GUARDS_NUM=10
guards=[]
dire=[]
for i in range(GUARDS_NUM):
    g=Circle(Point(WIDTH-60,HEIGHT-60),10)
    g.setFill('blue')
    g.draw(win)
    guards.append(g)
    d=[0,0]
    dire.append(d)
for x in range(0,WIDTH,50):
    for y in range(0,HEIGHT,50):
        r=Rectangle(Point(x,y),Point(x+30,y+30))
        r.setFill('red')
        r.draw(win)
player=Circle(Point(40,40),10)
player.setFill('yellow')
player.draw(win)
xval,yval=0,0
MOVE=[-1,0,1]
target=Rectangle(Point(WIDTH-20,HEIGHT-20),Point(WIDTH,HEIGHT))
target.setFill('green')
target.draw(win)
while(True):
    s=win.checkKey()
    xval,yval=0,0
    if(s!=None):
        if(s=="Up"):
            xval=0
            yval=-50
        elif(s=="Down"):
            xval=0
            yval=50
        elif(s=="Left"):
            xval=-50
            yval=0
        elif(s=="Right"):
            xval=50
            yval=0
        cen=player.getCenter()
        X=cen.getX()+xval
        Y=cen.getY()+yval
        if(X>=0 and X<=WIDTH and Y>=0 and Y<=HEIGHT):
            player.move(xval,yval)
        if(cen.getX()==WIDTH-10 and cen.getY()==HEIGHT-10):
            winner()
    for i in range(GUARDS_NUM):
        cen=guards[i].getCenter()
        X=cen.getX()
        Y=cen.getY()
        if(((X-40)%50==0 and (Y-40)%50==0) or (dire[i][0]==0 and dire[i][1]==0)):
            while(True):
                x=random.randint(0,2)
                y=random.randint(0,2)
                if(x==1 or y==1):
                    break
            dire[i][0],dire[i][1]=MOVE[x],MOVE[y]
        X=X+(dire[i][0]*GUARD_MOVE)
        Y=Y+(dire[i][1]*GUARD_MOVE)
        if(X>=10 and X<=WIDTH-10 and Y>=10 and Y<=HEIGHT-10):
            guards[i].move(dire[i][0]*GUARD_MOVE,dire[i][1]*GUARD_MOVE)
        else:
            dire[i][0],dire[i][1]=(-1)*dire[i][0],(-1)*dire[i][1]
            guards[i].move(dire[i][0]*GUARD_MOVE,dire[i][1]*GUARD_MOVE)
        pcen=player.getCenter()
        gcen=guards[i].getCenter()
        pX,pY=pcen.getX(),pcen.getY()
        gX,gY=gcen.getX(),gcen.getY()
        if(pX==gX):
            diff=abs(pY-gY)
            if(diff<20):
                game_over()
        elif(pY==gY):
            diff=abs(pX-gX)
            if(diff<20):
                game_over()
    time.sleep(0.001)
