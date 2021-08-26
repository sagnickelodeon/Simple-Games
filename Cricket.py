def lose():
    global runs
    fi="You lost by "+str(target-sum(runs))+" runs"
    ou=Text(Point(int((WIDTH+XLEFT)/2),int(HEIGHT/2)),fi)
    ou.move(0,((-1)*int(HEIGHT/2))-40)
    ou.setSize(36)
    ou.setStyle('bold')
    ou.draw(win)
    outmove=5
    totmove=int((HEIGHT+80)/(2*outmove))
    for h in range(totmove):
        ou.move(0,outmove)
        time.sleep(0.01)

def won():
    global wickets
    global PLAYER_NUM
    fi="You won by "+str(PLAYER_NUM-wickets-1)+" wickets"
    ou=Text(Point(int((WIDTH+XLEFT)/2),int(HEIGHT/2)),fi)
    ou.move(0,((-1)*int(HEIGHT/2))-40)
    ou.setSize(36)
    ou.setStyle('bold')
    ou.draw(win)
    outmove=5
    totmove=int((HEIGHT+80)/(2*outmove))
    for h in range(totmove):
        ou.move(0,outmove)
        time.sleep(0.01)

def it4():
    ou=Text(Point(int((WIDTH+XLEFT)/2),int(HEIGHT/2)),"4")
    ou.move(0,((-1)*int(HEIGHT/2))-40)
    ou.setSize(36)
    ou.setStyle('italic')
    ou.draw(win)
    outmove=5
    totmove=int((HEIGHT+80)/outmove)
    for h in range(totmove):
        ou.move(0,outmove)
        if(h==int(totmove/2)):
            time.sleep(1)
        time.sleep(0.01)

def it6():
    ou=Text(Point(int((WIDTH+XLEFT)/2),int(HEIGHT/2)),"6")
    ou.move(0,((-1)*int(HEIGHT/2))-40)
    ou.setSize(36)
    ou.setStyle('italic')
    ou.draw(win)
    outmove=5
    totmove=int((HEIGHT+80)/outmove)
    for h in range(totmove):
        ou.move(0,outmove)
        if(h==int(totmove/2)):
            time.sleep(1)
        time.sleep(0.01)

def out():
    ou=Text(Point(int((WIDTH+XLEFT)/2),int(HEIGHT/2)),"OUT")
    ou.move(0,((-1)*int(HEIGHT/2))-40)
    ou.setSize(36)
    ou.setStyle('italic')
    ou.draw(win)
    outmove=5
    totmove=int((HEIGHT+80)/outmove)
    for h in range(totmove):
        ou.move(0,outmove)
        if(h==int(totmove/2)):
            time.sleep(1)
        time.sleep(0.01)

def update_score(ov):
    global runs
    global onfield
    global total_score
    global overs
    global wickets
    global pl
    global batsmen
    total_score.undraw()
    overs.undraw()
    total=sum(runs)
    sc=str(total)+"/"+str(wickets)
    complete=int(ov/6)
    ongoing=ov%6
    o=str(complete)+"."+str(ongoing)
    total_score=Text(Point(int(XLEFT/2),100),sc)
    total_score.setSize(36)
    total_score.setTextColor('white')
    total_score.draw(win)
    overs=Text(Point(int(XLEFT/2),140),o)
    overs.setSize(20)
    overs.setTextColor('white')
    overs.draw(win)
    l=Line(Point(0,170),Point(XLEFT,170))
    l.setWidth(3)
    l.setFill('white')
    l.draw(win)
    for yt in batsmen:
        yt.undraw()
    batsmen=[]
    for yt in range(len(runs)):
        fir="Player "+str(yt+1)+"        "+str(runs[yt])
        if(onfield[yt]==True):
            fir=fir+"*"
        else:
            fir=fir+" "
        pl=Text(Point(int(XLEFT/2),185+yt*35),fir)
        pl.setSize(25)
        pl.setTextColor('white')
        pl.draw(win)
        batsmen.append(pl)

def generate():
    global ballmove
    while(True):
        x=random.randint(0,len(ballmove)-1)
        y=random.randint(0,len(ballmove)-1)
        if(x!=4 or y!=4):
            break
    return (x,y)

def distance(a,b):
    ax,ay=a.getX(),a.getY()
    bx,by=b.getX(),b.getY()
    return math.sqrt((ax-bx)**2+(ay-by)**2)

def setPlayer():
    global PLAYER_NUM
    pnum=PLAYER_NUM
    txt=Text(Point(int(WIDTH/2),int(HEIGHT/2)-30),"Enter number of players")
    txt.setTextColor('white')
    txt.setSize(25)
    txt.draw(win)
    pl=Text(Point(int(WIDTH/2),int(HEIGHT/2)+20),str(pnum))
    pl.setTextColor('white')
    pl.setSize(20)
    pl.draw(win)
    xmid,ymid=int(WIDTH/2),int(HEIGHT/2)
    arrowleftleft=xmid-50
    arrowlefttop=ymid+5
    arrowleftright=xmid-30
    arrowleftbottom=ymid+35
    arrowrightleft=xmid+30
    arrowrighttop=ymid+5
    arrowrightright=xmid+50
    arrowrightbottom=ymid+35
    leftrect=Rectangle(Point(arrowleftleft,arrowlefttop),Point(arrowleftright,arrowleftbottom))
    leftrect.setFill('white')
    leftrect.draw(win)
    rightrect=Rectangle(Point(arrowrightleft,arrowrighttop),Point(arrowrightright,arrowrightbottom))
    rightrect.setFill('white')
    rightrect.draw(win)
    leftar=Text(Point(int(arrowleftright+arrowleftleft)/2,int(arrowleftbottom+arrowlefttop)/2),"<")
    leftar.setTextColor('black')
    leftar.setStyle('bold')
    leftar.setSize(25)
    leftar.draw(win)
    rightar=Text(Point(int(arrowrightright+arrowrightleft)/2,int(arrowrightbottom+arrowrighttop)/2),">")
    rightar.setTextColor('black')
    rightar.setStyle('bold')
    rightar.setSize(25)
    rightar.draw(win)
    #okaycir=Circle(Point(xmid,ymid+120),60)
    #okaycir.setFill('white')
    #okaycir.draw(win)
    okay=Text(Point(xmid,ymid+120),"Press 'Enter' when done")
    okay.setStyle('bold')
    okay.setSize(28)
    okay.setTextColor('white')
    okay.draw(win)
    while(True):
        s=win.checkKey()
        if(s==None):
            continue
        if(s=="Left" and pnum>3):
            pl.undraw()
            pnum=pnum-1
            pl=Text(Point(int(WIDTH/2),int(HEIGHT/2)+20),str(pnum))
            pl.setTextColor('white')
            pl.setSize(20)
            pl.draw(win)
        elif(s=="Right" and pnum<11):
            pl.undraw()
            pnum=pnum+1
            pl=Text(Point(int(WIDTH/2),int(HEIGHT/2)+20),str(pnum))
            pl.setTextColor('white')
            pl.setSize(20)
            pl.draw(win)
        elif(s=="Return"):
            PLAYER_NUM=pnum
            break
    #    time.sleep(6)
    okay.undraw()
    txt.undraw()
    

from graphics import *
import random
import math

WIDTH,HEIGHT=900,650
XLEFT=WIDTH-HEIGHT
PLAYER_NUM=3
BALL_SPEED=5
OVERS=5
BOWLER_SPEED=1
FIELDER_SPEED=4
STUMPS=50
RUNNER_SPEED=35

fielders=[]
runs=[]
xmid,ymid=int((WIDTH+XLEFT)/2),int(HEIGHT/2)
mwin=False

win=GraphWin("Cricket",WIDTH,HEIGHT)
win.setBackground('black')
setPlayer()
rect=Rectangle(Point(XLEFT,0),Point(WIDTH,HEIGHT))
rect.setFill('green')
rect.draw(win)
bound=Circle(Point(xmid,ymid),int(HEIGHT/2))#Oval(Point(XLEFT,0),Point(WIDTH-1,HEIGHT-1))
bound.setWidth(3)
bound.setOutline('white')
bound.draw(win)
xmid,ymid=int((WIDTH+XLEFT)/2),int(HEIGHT/2)
pitch=Line(Point(xmid,ymid-int(HEIGHT/14)),Point(xmid,ymid+int(HEIGHT/14)))
pitch.setWidth(int(HEIGHT/47))
pitch.setFill('navajowhite')
pitch.draw(win)
smallradius=int(HEIGHT/14)
bigradius=bound.getRadius()
#print(smallradius,bigradius)
cen=bound.getCenter()
for i in range(PLAYER_NUM-2):
    x,y=0,0
    while(True):
        x=random.randint(XLEFT+1,WIDTH)
        y=random.randint(1,HEIGHT)
        dist=distance(cen,Point(x,y))
        if(dist>(smallradius+50) and dist<bigradius):
            break
    pl=Circle(Point(x,y),3)
    pl.setFill('black')
    pl.draw(win)
    fielders.append(pl)
p1=Circle(Point(xmid,ymid-int(HEIGHT/14)-35),3)
p1.setFill('black')
p1.draw(win)
fielders.append(p1)
bowler=len(fielders)-1
p1=Circle(Point(xmid,ymid+int(HEIGHT/14)+5),3)
p1.setFill('black')
p1.draw(win)
fielders.append(p1)

p1=Circle(Point(xmid,ymid+int(HEIGHT/14)-3),3)
p1.setFill('red')
p1.draw(win)
runs.append(0)
strike=0
p2=Circle(Point(xmid,ymid-int(HEIGHT/14)+3),3)
p2.setFill('red')
p2.draw(win)
runs.append(0)
nstrike=1
ball=Circle(Point(xmid,ymid-int(HEIGHT/14)-35),3)
ball.setFill('white')
ball.draw(win)

ballinbowler=True
ballinpitch=True
ballinmovement=False
playerthrow=False
ownside=True

onfield=[True,True]
ballmove=[-6,-4,-3,0,3,4,6]
a,b=0,0
who=0
bg,s1,s2,r1,r2=0,0,0,0,0
total_score=Circle(Point(1,1),9)
total_score.draw(win)
overs=Circle(Point(1,1),9)
wickets=0
overs.draw(win)
target=int(random.randint(60,80)*OVERS/10)
tar="Target: "+str(target+1)
t=Text(Point(int(XLEFT/2),30),tar)
t.setStyle('bold')
t.setTextColor('white')

batsmen=[]
#pl1=Text(Point(1,1),"gjghv")
#pl1.draw(win)
pl=Text(Point(1,1),"gjghv")
pl.draw(win)
batsmen.append(pl)

t.setSize(30)
t.draw(win)
update_score(0)
for iloop in range(OVERS*6):
    pressed=False
    firstpress=False
    singles=0
    while(True):
        time.sleep(0.05)
        if(ballinbowler==True):
            y=fielders[bowler].getCenter().getY()
            if(y<(ymid-int(HEIGHT/14))):
                fielders[bowler].move(0,BOWLER_SPEED)
                ball.move(0,BOWLER_SPEED)
                continue
            else:
                ballinbowler=False
        firstpress=False
        s=win.checkKey()
        if(s=='x' and pressed==False):
            firstpress=True
            pressed=True
        if(ballinmovement==True):
            if(s=="Up" and rs.getCenter().getY()>35):
                rs.move(0,-1*RUNNER_SPEED)
                rns.move(0,RUNNER_SPEED)
                if(ownside==True):
                    rsy=rs.getCenter().getY()
                    if(rsy<STUMPS+20):
                        singles=singles+1
                        ownside=False
            elif(s=="Down" and rs.getCenter().getY()<HEIGHT-35):
                rs.move(0,RUNNER_SPEED)
                rns.move(0,-1*RUNNER_SPEED)
                if(ownside==False):
                    rsy=rs.getCenter().getY()
                    if(rsy>HEIGHT-STUMPS-20):
                        singles=singles+1
                        ownside=True
        if(ballinpitch==True):
            y=ball.getCenter().getY()
            Y=p1.getCenter().getY()
            if((y>=Y-20 and y<=Y+2) and s=='x' and firstpress==True):
                a,b=generate()
                ballinmovement=True
                ballinpitch=False
                bg=Rectangle(Point(0,0),Point(XLEFT,HEIGHT))
                bg.setFill('navajowhite')
                bg.draw(win)
                s1=Line(Point(0,STUMPS),Point(XLEFT,STUMPS))
                s1.setWidth(3)
                s1.setFill('black')
                s1.draw(win)
                s2=Line(Point(0,HEIGHT-STUMPS),Point(XLEFT,HEIGHT-STUMPS))
                s2.setWidth(3)
                s2.setFill('black')
                s2.draw(win)
                rns=Circle(Point(int(XLEFT*3/4),STUMPS-20),20)
                rns.setFill('red')
                rns.draw(win)
                rs=Circle(Point(int(XLEFT/4),HEIGHT-STUMPS+20),20)
                rs.setFill('red')
                rs.draw(win)
                
            else:
                ball.move(0,BALL_SPEED)
        bally=ball.getCenter().getY()
        if(bally>=(bound.getCenter().getY()+smallradius) and ballinmovement==False):
            ball.undraw()
            ball=Circle(fielders[len(fielders)-1].getCenter(),3)
            ball.setFill('white')
            ball.draw(win)
            p=random.randint(0,100)
            if(p<50):
                out()
                wickets=wickets+1
                runs.append(0)
                onfield[strike]=False
                onfield.append(True)
                strike=len(runs)-1
            break
        if(ballinmovement==True):
            ball.move(ballmove[a],ballmove[b])
        mind=HEIGHT
        for j in range(PLAYER_NUM-1):
            dist=distance(fielders[j].getCenter(),ball.getCenter())
            if(dist<mind):
                mind=dist
                who=j
        bX,bY=ball.getCenter().getX(),ball.getCenter().getY()
        oX,oY=fielders[who].getCenter().getX(),fielders[who].getCenter().getY()
        oppox,oppoy=0,0
        if(bX<oX):
            oppox=(-1)*FIELDER_SPEED
        elif(bX>oX):
            oppox=FIELDER_SPEED
        if(bY<oY):
            oppoy=(-1)*FIELDER_SPEED
        elif(bY>oY):
            oppoy=FIELDER_SPEED
        if(ballinmovement==True and playerthrow==False):
            fielders[who].move(oppox,oppoy)
            dist=distance(fielders[who].getCenter(),ball.getCenter())
            if(dist<6):
                playerthrow=True
                a=len(ballmove)-1-a
                b=len(ballmove)-1-b
        if(playerthrow==True):
            dist=distance(fielders[len(fielders)-1].getCenter(),ball.getCenter())
            if(dist<25):
                ball.undraw()
                ball=Circle(fielders[len(fielders)-1].getCenter(),3)
                ball.setFill('white')
                ball.draw(win)
                rsy=rs.getCenter().getY()
                if(rsy<(HEIGHT-STUMPS-20) and rsy>STUMPS+20):
                    out()
                    wickets=wickets+1
                    runs.append(0)
                    onfield[strike]=False
                    onfield.append(True)
                    strike=len(runs)-1
                bg.undraw()
                s1.undraw()
                s2.undraw()
                rs.undraw()
                rns.undraw()
                break
        bcen=bound.getCenter()
        cen=ball.getCenter()
        dist=distance(cen,bcen)
        if(dist>ymid):
            singles=0
            pro=random.randint(0,100)
            if(pro<=70):
                it4()
                runs[strike]=runs[strike]+4
            else:
                it6()
                runs[strike]=runs[strike]+6
            bg.undraw()
            s1.undraw()
            s2.undraw()
            rs.undraw()
            rns.undraw()
            break
    for i in range(PLAYER_NUM):
        fielders[i].undraw()
    ball.undraw()
    fielders=[]
    if(singles>0):
        runs[strike]=runs[strike]+singles
        if(singles%2==1):
            strike,nstrike=nstrike,strike
    print(runs)
    for i in range(PLAYER_NUM-2):
        x,y=0,0
        while(True):
            x=random.randint(XLEFT+1,WIDTH)
            y=random.randint(1,HEIGHT)
            dist=distance(cen,Point(x,y))
            if(dist>(smallradius+50) and dist<bigradius):
                break
        pl=Circle(Point(x,y),3)
        pl.setFill('black')
        pl.draw(win)
        fielders.append(pl)
    p1=Circle(Point(xmid,ymid-int(HEIGHT/14)-35),3)
    p1.setFill('black')
    p1.draw(win)
    fielders.append(p1)
    bowler=len(fielders)-1
    p1=Circle(Point(xmid,ymid+int(HEIGHT/14)+5),3)
    p1.setFill('black')
    p1.draw(win)
    fielders.append(p1)
    ball=Circle(Point(xmid,ymid-int(HEIGHT/14)-35),3)
    ball.setFill('white')
    ball.draw(win)
    ballinbowler=True
    ballinpitch=True
    ballinmovement=False
    playerthrow=False
    ownside=True
    if(wickets==PLAYER_NUM-1):
        break
    update_score(iloop+1)
    if(sum(runs)>target):
        mwin=True
        break
    
if(mwin==False):
    lose()
else:
    won()
print(sum(runs),target,mwin)
            
            
