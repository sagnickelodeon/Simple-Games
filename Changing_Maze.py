def won():
    re=Rectangle(Point(0,int((HEIGHT-YLOW)/4+YLOW)),Point(WIDTH,int(3*(HEIGHT-YLOW)/4+YLOW)))
    re.setFill('white')
    re.draw(win)
    txt=Text(Point(int(WIDTH/2),int((HEIGHT-YLOW)/2)+YLOW-20),"YOU WIN")
    txt.setSize(30)
    txt.setStyle('italic')
    txt.setTextColor('black')
    txt.move((-1)*WIDTH,0)
    txt.draw(win)
    con=Text(Point(int(WIDTH/2),int((HEIGHT-YLOW)/2)+YLOW+20),"Congratulations!")
    con.setSize(30)
    con.setStyle('italic')
    con.setTextColor('black')
    con.move(WIDTH,0)
    con.draw(win)
    while(True):
        txt.move(5,0)
        con.move(-5,0)
        x,y=txt.getAnchor().getX(),txt.getAnchor().getY()
        if(x>=int(WIDTH/2)):
            break
        time.sleep(0.01)

from graphics import *
import random
import math

YLOW=0
WIDTH,HEIGHT=1000,600+YLOW
CHANCE=50
SQUARE=100
PMOVE=SQUARE

walls=[]
walls_moving=[]
wallnext=[]
whonext=[]
wall_dir=[]
wall_center=[]
wallnum=0
pexist=False
texist=False

prange=int(WIDTH/4)
trange=int(3*WIDTH/4)
win=GraphWin("Change",WIDTH,HEIGHT)
win.setBackground('black')
player=Circle(Point(0,0),5)
target=Rectangle(Point(0,0),Point(1,1))
for x in range(0,WIDTH,SQUARE):
    for y in range(YLOW,HEIGHT,SQUARE):
        prob=random.randint(1,100)
        if(prob<=CHANCE):
            rec=Rectangle(Point(x,y),Point(x+SQUARE,y+SQUARE))
            rec.setFill('red')
            rec.draw(win)
            wallnum=wallnum+1
            walls.append(rec)
            wall_center.append([x+int(SQUARE/2),y+int(SQUARE/2)])
        else:
            prob=random.randint(1,100)
            if(x<prange and prob<=70 and pexist==False):
                player=Circle(Point(x+int(SQUARE/2),y+int(SQUARE/2)),int(SQUARE/2))
                player.setFill('yellow')
                player.draw(win)
                pexist=True
            if(x>trange and prob<=70 and texist==False):
                target=Rectangle(Point(x,y),Point(x+SQUARE,y+SQUARE))
                target.setFill('blue')
                target.draw(win)
                texist=True
for i in range(wallnum):
    walls_moving.append(False)
xval,yval=0,0
WM=50
wmove=[(-1)*WM,0,WM]
t0=time.clock()
while(True):
    s=win.checkKey()
    xval=0
    yval=0
    correct=False
    if(s==None):
        continue
    if(s=="Up"):
        correct=True
        xval=0
        yval=(-1)*PMOVE
    elif(s=="Down"):
        correct=True
        xval=0
        yval=PMOVE
    elif(s=="Left"):
        correct=True
        xval=(-1)*PMOVE
        yval=0
    elif(s=="Right"):
        correct=True
        xval=PMOVE
        yval=0
    t1=time.clock()
    #if(t1-t0>=.5):
    #   t0=t1
        #for i in range(wallnum):
        #    walls[i].undraw()
        #walls=[]
        #wallnum=0
        #for x in range(0,WIDTH,SQUARE):
        #    for y in range(YLOW,HEIGHT,SQUARE):
        #        prob=random.randint(1,100)
        #        px,py=player.getCenter().getX(),player.getCenter().getY()
        #        tx,ty=target.getCenter().getX(),target.getCenter().getY()
        #        X,Y=x+int(SQUARE/2),y+int(SQUARE/2)
        #        if((X==px and Y==py) or (X==tx and Y==ty)):
        #            continue
        #        if(prob<=CHANCE):
        #            rec=Rectangle(Point(x,y),Point(x+SQUARE,y+SQUARE))
        #            rec.setFill('red')
        #            rec.draw(win)
        #            wallnum=wallnum+1
        #            walls.append(rec)
        #for i in range(wallnum):
        #    x,y=0,0
        #    while(True):
        #        x=random.randint(0,2)
        #        y=random.randint(0,2)
        #        if(x==1 or y==1):
        #            break
        #    X,Y=walls[i].getCenter().getX()+wmove[x],walls[i].getCenter().getY()+wmove[y]
        #    px,py=player.getCenter().getX(),player.getCenter().getY()
        #    tx,ty=target.getCenter().getX(),target.getCenter().getY()
        #    if(X>=int(SQUARE/2) and X<=(WIDTH-int(SQUARE/2)) and Y>=(YLOW+int(SQUARE/2)) and Y<=(HEIGHT-int(SQUARE/2))):
        #        if((X==px and Y==py) or (X==tx and Y==ty)):
        #            continue
        #        walls[i].move(wmove[x],wmove[y])
    if(correct==True):
        for i in range(wallnum):
            walls[i].undraw()
        walls=[]
        wallnum=0
        for x in range(0,WIDTH,SQUARE):
            for y in range(YLOW,HEIGHT,SQUARE):
                prob=random.randint(1,100)
                px,py=player.getCenter().getX(),player.getCenter().getY()
                tx,ty=target.getCenter().getX(),target.getCenter().getY()
                X,Y=x+int(SQUARE/2),y+int(SQUARE/2)
                if((X==px and Y==py) or (X==tx and Y==ty)):
                    continue
                if(prob<=CHANCE):
                    rec=Rectangle(Point(x,y),Point(x+SQUARE,y+SQUARE))
                    rec.setFill('red')
                    rec.draw(win)
                    wallnum=wallnum+1
                    walls.append(rec)
    X,Y=player.getCenter().getX()+xval,player.getCenter().getY()+yval
    flag=False
    for i in range(wallnum):
        wx,wy=walls[i].getCenter().getX(),walls[i].getCenter().getY()
        if(X==wx and Y==wy):
            flag=True
            break
    if(flag==True):
        continue
    if(X>=int(SQUARE/2) and X<=(WIDTH-int(SQUARE/2)) and Y>=(YLOW+int(SQUARE/2)) and Y<=(HEIGHT-int(SQUARE/2)) and correct==True):
        player.move(xval,yval)
    px,py=player.getCenter().getX(),player.getCenter().getY()
    tx,ty=target.getCenter().getX(),target.getCenter().getY()
    if(px==tx and py==ty):
        won()
        break
    time.sleep(0.01)
