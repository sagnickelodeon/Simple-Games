def update_score():
    global score
    global player_score
    global opponent_score
    score.undraw()
    pl=str(player_score)
    mid="-"
    op=str(opponent_score)
    final=pl+mid+op
    score=Text(Point(int(WIDTH/2),HEIGHT-40),final)
    score.setTextColor('white')
    score.setSize(30)
    score.setStyle('bold')
    score.draw(win)

def delete():
    for i in range(PLAYER_NUM):
        own[i].undraw()
        opponent[i].undraw()
    ball.undraw()

def randomize():
    global ball
    global own
    own=[]
    global opponent
    opponent=[]
    global balldir
    balldir=[int(OWN_MOVE),0]
    global correct
    correct=False
    global ballinplayer
    ballinplayer=True
    global ballinmovement
    ballinmovement=False
    global positionx
    positionx=[]
    global positiony
    positiony=[]
    global oppopositionx
    oppopositionx=[]
    global selfball
    selfball=True
    global shot
    shot=False
    for i in range(BALL_SIZE*2+int(PLAYER_SIZE/2),int(WIDTH/2),OWN_MOVE):
        positionx.append(i)
    for i in range(BALL_SIZE*2+int(PLAYER_SIZE/2),int(HEIGHT)-BALL_SIZE*2-int(PLAYER_SIZE/2),OWN_MOVE):
        positiony.append(i)
    for i in range(int(WIDTH/2)+BALL_SIZE*2+int(PLAYER_SIZE/2),int(WIDTH)-BALL_SIZE*2-int(PLAYER_SIZE/2),OWN_MOVE):
        oppopositionx.append(i)
        
    for i in range(PLAYER_NUM):
        x=random.randint(0,len(positionx)-1)
        y=random.randint(0,len(positiony)-1)
        p=Line(Point(positionx[x]-int(PLAYER_SIZE/2),positiony[y]),Point(positionx[x]+int(PLAYER_SIZE/2),positiony[y]))
        p.setWidth(PLAYER_SIZE)
        p.setFill('red')
        p.draw(win)
        own.append(p)
    for i in range(PLAYER_NUM):
        x=random.randint(0,len(oppopositionx)-1)
        y=random.randint(0,len(positiony)-1)
        p=Line(Point(oppopositionx[x]-int(PLAYER_SIZE/2),positiony[y]),Point(oppopositionx[x]+int(PLAYER_SIZE/2),positiony[y]))
        p.setWidth(PLAYER_SIZE)
        p.setFill('blue')
        p.draw(win)
        opponent.append(p)
    who=random.randint(0,PLAYER_NUM-1)
    cen=own[who].getCenter()
    X,Y=cen.getX(),cen.getY()
    ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
    ball.setFill('white')
    ball.draw(win)
    howfar=0

def player_goal():
    col=['red','yellow']
    global player_score
    player_score=player_score+1
    global win
    for i in range(20):
        cir=Circle(Point(int(WIDTH/2),int(HEIGHT/2)),100+i*BALL_SIZE)
        cir.setFill('green')
        cir.draw(win)
        goal=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"GOAL!")
        goal.setTextColor(col[i%2])
        goal.setSize(30)
        goal.setStyle('bold')
        goal.draw(win)
        time.sleep(0.2)
        cir.undraw()
        goal.undraw()
    update_score()
    delete()
    randomize()

def opponent_goal():
    col=['black','white']
    global opponent_score
    opponent_score=opponent_score+1
    global win
    for i in range(20):
        cir=Circle(Point(int(WIDTH/2),int(HEIGHT/2)),140+i*BALL_SIZE)
        cir.setFill('green')
        cir.draw(win)
        goal=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"Heh..GOAL??")
        goal.setTextColor(col[i%2])
        goal.setSize(30)
        goal.setStyle('bold')
        goal.draw(win)
        time.sleep(0.2)
        cir.undraw()
        goal.undraw()
    update_score()
    delete()
    randomize()

def move_oppo():
    if(selfball==False):
        correct=False
        global ball
        global shot
        global ballinplayer
        global ballinmovement
        global balldir
        pX,pY=own[who].getCenter().getX(),own[who].getCenter().getY()
        oX,oY=opponent[other].getCenter().getX(),opponent[other].getCenter().getY()
        xval=0
        yval=0
        s="Left"
        if(((pX-oX)<=0 and (pX-oX)>-45) and ((pY-oY)<30 and (pY-oY)>-30)):
            s="Left"
        elif(((pX-oX)<30 and (pX-oX)>-30) and ((pY-oY)>=-45 and (pY-oY)<=0)):
            s="Up"
        elif(((pX-oX)<=45 and (pX-oX)>=0) and ((pY-oY)<30 and (pY-oY)>-30)):
            s="Right"
        elif(((pX-oX)<30 and (pX-oX)>-30) and ((pY-oY)<=45 and (pY-oY)>=0)):
            s="Down"
        if(s=="Up"):
            correct=True
            xval=0
            yval=(-1)*OPPO_MOVE*MUL
            if(ballinplayer==True):
                ball.undraw()
                cen=opponent[other].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X,Y-int(PLAYER_SIZE/2)-BALL_SIZE),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Down"):
            correct=True
            xval=0
            yval=OPPO_MOVE*MUL
            if(ballinplayer==True):
                ball.undraw()
                cen=opponent[other].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X,Y+int(PLAYER_SIZE/2)+BALL_SIZE),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Left"):
            correct=True
            xval=(-1)*OPPO_MOVE*MUL
            yval=0
            if(ballinplayer==True):
                ball.undraw()
                cen=opponent[other].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X-int(PLAYER_SIZE/2)-BALL_SIZE,Y),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Right"):
            correct=True
            xval=(-1)*OPPO_MOVE*MUL
            yval=0
            if(ballinplayer==True):
                ball.undraw()
                cen=opponent[other].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X-int(PLAYER_SIZE/2)-BALL_SIZE,Y),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        
        shoot_point=Point(150,int(HEIGHT/2))
        cen=opponent[other].getCenter()
        X,Y=cen.getX(),cen.getY()
        if(X>150):
            if(Y<TOP):
                yval=OPPO_MOVE*MUL
            elif(Y>BOTTOM):
                yval=(-1)*OPPO_MOVE*MUL
        elif(X<=150):
            if(Y<TOP):
                yval=OPPO_MOVE*MUL
            elif(Y>BOTTOM):
                yval=(-1)*OPPO_MOVE*MUL
            else:
                ballinmovement=True
                shot=True
                #print("Function")
        #elif(s=="Right"):
        #    correct=True
        #    xval=OPPO_MOVE*MUL
        #    yval=0
        #    if(ballinplayer==True):
        #        ball.undraw()
        #        cen=opponent[other].getCenter()
        #        X,Y=cen.getX(),cen.getY()
        #        ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
        #        ball.setFill('white')
        #        ball.draw(win)
        if(correct==True):
            cen=opponent[other].getCenter()
            X,Y=cen.getX(),cen.getY()
            X=X+xval
            Y=Y+yval
            if(X>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and X<=(WIDTH-BALL_SIZE*2-int(PLAYER_SIZE/2)) and Y>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and Y<=(HEIGHT-BALL_SIZE*2-int(PLAYER_SIZE/2))):
                opponent[other].move(xval,yval)
                if(ballinplayer==True):
                    ball.move(xval,yval)
                    balldir[0]=int(xval/2)*MUL*3
                    balldir[1]=int(yval/2)*MUL*3
        if(ballinmovement==True):
            ballinplayer=False

def distance(a,b):
    aX,bX=a.getX(),b.getX()
    aY,bY=a.getY(),b.getY()
    return math.sqrt((aX-bX)**2+(aY-bY)**2)

def decision():
    global player_score
    global opponent_score
    if(player_score<opponent_score):
        de=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"YOU LOSE. IDIOT.")
    elif(player_score>opponent_score):
        de=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"YOU WIN! CONGRATULATIONS!")
    else:
        de=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"IT'S A DRAW. MEH")
    de.setTextColor('white')
    de.setSize(30)
    de.draw(win)
    time.sleep(3)

def update_time():
    global minutes
    global seconds
    global t
    t.undraw()
    if(minutes<10):
        f="0"+str(minutes)
    else:
        f=str(minutes)
    m=":"
    if(seconds<10):
        l="0"+str(seconds)
    else:
        l=str(seconds)
    fin=f+m+l
    t=Text(Point(int(WIDTH/2),40),fin)
    t.setTextColor('white')
    t.setSize(30)
    #t.setStyle('bold')
    t.draw(win)

from graphics import *
import random
import math

WIDTH,HEIGHT=1000,600
PLAYER_NUM=5
PLAYER_SIZE=30
BALL_SIZE=10
OWN_MOVE=10
OPPO_MOVE=2
OPPO_SHOOT=150
MUL=1
TOP,BOTTOM=int(HEIGHT/2)-70,int(HEIGHT/2)+70
LEFT,RIGHT=BALL_SIZE*2,WIDTH-BALL_SIZE*2

win=GraphWin("Football",WIDTH,HEIGHT)
win.setBackground('black')

own=[]
opponent=[]
balldir=[int(OWN_MOVE/4),0]
correct=False
ballinplayer=True
ballinmovement=False
positionx=[]
positiony=[]
oppopositionx=[]
selfball=True
shot=False
player_score,opponent_score=0,0
score=Text(Point(200,200),"ABCDE")
score.draw(win)
update_score()

for i in range(BALL_SIZE*2+int(PLAYER_SIZE/2),int(WIDTH/2),OWN_MOVE):
    positionx.append(i)
for i in range(BALL_SIZE*2+int(PLAYER_SIZE/2),int(HEIGHT)-BALL_SIZE*2-int(PLAYER_SIZE/2),OWN_MOVE):
    positiony.append(i)
for i in range(int(WIDTH/2)+BALL_SIZE*2+int(PLAYER_SIZE/2),int(WIDTH)-BALL_SIZE*2-int(PLAYER_SIZE/2),OWN_MOVE):
    oppopositionx.append(i)

goal_left=Line(Point(BALL_SIZE,int(HEIGHT/2)-70),Point(BALL_SIZE,int(HEIGHT/2)+70))
goal_left.setWidth(BALL_SIZE*2)
goal_left.setFill('green')
goal_left.draw(win)
goal_right=Line(Point(WIDTH-BALL_SIZE,int(HEIGHT/2)-70),Point(WIDTH-BALL_SIZE,int(HEIGHT/2)+70))
goal_right.setWidth(BALL_SIZE*2)
goal_right.setFill('green')
goal_right.draw(win)

for i in range(PLAYER_NUM):
    x=random.randint(0,len(positionx)-1)
    y=random.randint(0,len(positiony)-1)
    p=Line(Point(positionx[x]-int(PLAYER_SIZE/2),positiony[y]),Point(positionx[x]+int(PLAYER_SIZE/2),positiony[y]))
    p.setWidth(PLAYER_SIZE)
    p.setFill('red')
    p.draw(win)
    own.append(p)
for i in range(PLAYER_NUM):
    x=random.randint(0,len(oppopositionx)-1)
    y=random.randint(0,len(positiony)-1)
    p=Line(Point(oppopositionx[x]-int(PLAYER_SIZE/2),positiony[y]),Point(oppopositionx[x]+int(PLAYER_SIZE/2),positiony[y]))
    p.setWidth(PLAYER_SIZE)
    p.setFill('blue')
    p.draw(win)
    opponent.append(p)
who=random.randint(0,PLAYER_NUM-1)
cen=own[who].getCenter()
X,Y=cen.getX(),cen.getY()
ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
ball.setFill('white')
ball.draw(win)
howfar=0
t0=time.clock()
minutes,seconds=2,0
t=Text(Point(1,1),"ABS")
t.draw(win)
update_time()
cout=0
while(True):
    t1=time.clock()
    if(t1-t0>=1):
        t0=t1
        seconds=seconds-1
        if(seconds<0):
            minutes=minutes-1
            seconds=59
        if(minutes<0):
            decision()
            win.close()
        update_time()
    s=win.checkKey()
    xval,yval=0,0
    correct=False
    if(s!=None and s!='x'):
        if(s=="Up"):
            correct=True
            xval=0
            yval=(-1)*OWN_MOVE
            if(ballinplayer==True and selfball==True):
                ball.undraw()
                cen=own[who].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X,Y-int(PLAYER_SIZE/2)-BALL_SIZE),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Down"):
            correct=True
            xval=0
            yval=OWN_MOVE
            if(ballinplayer==True and selfball==True):
                ball.undraw()
                cen=own[who].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X,Y+int(PLAYER_SIZE/2)+BALL_SIZE),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Left"):
            correct=True
            xval=(-1)*OWN_MOVE
            yval=0
            if(ballinplayer==True and selfball==True):
                ball.undraw()
                cen=own[who].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X-int(PLAYER_SIZE/2)-BALL_SIZE,Y),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        elif(s=="Right"):
            correct=True
            xval=OWN_MOVE
            yval=0
            if(ballinplayer==True and selfball==True):
                ball.undraw()
                cen=own[who].getCenter()
                X,Y=cen.getX(),cen.getY()
                ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
                ball.setFill('white')
                ball.draw(win)
        if(correct==True):
            cen=own[who].getCenter()
            X,Y=cen.getX(),cen.getY()
            X=X+xval
            Y=Y+yval
            if(X>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and X<=(WIDTH-BALL_SIZE*2-int(PLAYER_SIZE/2)) and Y>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and Y<=(HEIGHT-BALL_SIZE*2-int(PLAYER_SIZE/2))):
                own[who].move(xval,yval)
                if(ballinplayer==True and selfball==True):
                    ball.move(xval,yval)
                    balldir[0]=int(xval/2)
                    balldir[1]=int(yval/2)
                    
    elif(s!=None and (s=='x' or s=='X')):
        if(ballinplayer==True):
            ballinplayer=False
            ballinmovement=True
    if(ballinplayer==False and ballinmovement==True):
        cen=ball.getCenter()
        #print("main")
        X,Y=cen.getX()+balldir[0],cen.getY()+balldir[1]
        if(X>=(BALL_SIZE) and X<=(WIDTH-(BALL_SIZE)) and Y>=(BALL_SIZE) and Y<=(HEIGHT-BALL_SIZE)):
            ball.move(balldir[0],balldir[1])
            #print(balldir)
            #print("main")
        else:
            balldir[0],balldir[1]=[0,0]
            ballinmovement=False
        howfar=howfar+1
        #print(howfar)
        
    diff=WIDTH
    for i in range(PLAYER_NUM):
        temp=distance(own[i].getCenter(),ball.getCenter())
        if(temp<diff):
            diff=temp
            who=i
    cen=own[who].getCenter()
    dist=distance(cen,ball.getCenter())
    if(dist<=29 and howfar>=5 and (ballinplayer==False or selfball==False)):
        ball.undraw()
        cen=own[who].getCenter()
        X,Y=cen.getX(),cen.getY()
        ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
        ball.setFill('white')
        ball.draw(win)
        ballinplayer=True
        ballinmovement=False
        howfar=0
        selfball=True

    #From here, opponent player movement
    diff=WIDTH
    for i in range(PLAYER_NUM):
        temp=distance(opponent[i].getCenter(),ball.getCenter())
        if(temp<diff):
            diff=temp
            other=i
    oppox=0
    oppoy=0
    cen=ball.getCenter()
    oth=opponent[other].getCenter()
    bX,bY=cen.getX(),cen.getY()
    oX,oY=oth.getX(),oth.getY()
    if(bX>oX):
        oppox=int(OPPO_MOVE)
    elif(bX<oX):
        oppox=(-1)*int(OPPO_MOVE)
    if(bY>oY):
        oppoy=int(OPPO_MOVE)
    elif(bY<oY):
        oppoy=(-1)*int(OPPO_MOVE)
    X,Y=oX+oppox,oY+oppoy
    if(X>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and X<=(WIDTH-BALL_SIZE*2-int(PLAYER_SIZE/2)) and Y>=(BALL_SIZE*2+int(PLAYER_SIZE/2)) and Y<=(HEIGHT-BALL_SIZE*2-int(PLAYER_SIZE/2))):
        if(selfball==True):
            opponent[other].move(oppox,oppoy)
    cen=opponent[other].getCenter()
    dist=distance(cen,ball.getCenter())
    if(dist<=29 and (ballinplayer==False or selfball==True) and shot==False):
        ball.undraw()
        cen=opponent[other].getCenter()
        X,Y=cen.getX(),cen.getY()
        ball=Circle(Point(X+int(PLAYER_SIZE/2)+BALL_SIZE,Y),BALL_SIZE)
        ball.setFill('white')
        ball.draw(win)
        ballinplayer=True
        ballinmovement=False
        howfar=5
        selfball=False
    if(shot==False):
        move_oppo()
    X,Y=ball.getCenter().getX(),ball.getCenter().getY()
    if(Y>(TOP-BALL_SIZE) and Y<(BOTTOM+BALL_SIZE)):
        if(X<=LEFT+BALL_SIZE):
            opponent_goal()
        elif(X>=RIGHT-BALL_SIZE):
            player_goal()
    time.sleep(0.01)
