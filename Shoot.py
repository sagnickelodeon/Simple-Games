from graphics import *
import random
import math

def check(n):
    global WIDTH
    n1=n
    while(True):
        if(WIDTH%n1==0):
            break
        n1=n1-1
    dif1=n-n1
    n2=n+1
    while(True):
        if(WIDTH%n2==0):
            break
        n2=n2+1
    dif2=n2-n
    if(dif1<dif2):
        return n1
    return n2

def rectan():
    p1=Point(int(WIDTH/4),int(HEIGHT/4))
    p2=Point(int(3*WIDTH/4),int(3*HEIGHT/4))
    re=Rectangle(p1,p2)
    re.setFill('white')
    re.draw(win)
    return

def you_win():
    global cou
    score=3000-cou**2
    f="Your score: "
    l=str(score)
    final=f+l
    rectan()
    col=['black','red','blue','green']
    for o in range(8):
        x=random.randint(0,3)
        y=random.randint(0,3)
        txt=Text(Point(int(WIDTH/2),int(HEIGHT/2)-30),"YOU WIN!")
        txt.setTextColor(col[x])
        txt.setSize(30)
        txt.setStyle('bold')
        txt.draw(win)
        txt1=Text(Point(int(WIDTH/2),int(HEIGHT/2)+30),final)
        txt1.setTextColor(col[y])
        txt1.setSize(20)
        #txt.setStyle('bold')
        txt1.draw(win)
        time.sleep(0.5)
        txt.undraw()
        txt1.undraw()
    win.close()

def you_lose():
    rectan()
    txt=Text(Point(int(WIDTH/2),int(HEIGHT/2)),"YOU LOSE")
    txt.setTextColor('black')
    txt.setSize(30)
    txt.setStyle('bold')
    txt.draw(win)
    time.sleep(4)
    win.close()

def distance(a,b):
    aX,aY=a.getX(),a.getY()
    bX,bY=b.getX(),b.getY()
    return math.sqrt((aX-bX)**2+(aY-bY)**2)

WIDTH,HEIGHT=1000,600
TOT_HEIGHT=630
CHANCE=30
PLAYER_MOVE=50
GUARD_NUM=5
GUARD_MOVE=2
SHOT_SPEED=5
GUARD_SHOT=5
HITS=check(20)
#print(HITS)

squares=0
span=WIDTH
howlong=int(span/HITS)
total=int(WIDTH/50)*int(HEIGHT/50)
exist=False
walls=[]
guards=[]
guard_shots=[]
gshot_dir=[]
gshot_exist=[]
flag=True
gmove=[]
options=[(-1)*GUARD_MOVE,0,GUARD_MOVE]
player_shots=[]
pshot_dir=[]

win=GraphWin("Shoot",WIDTH,TOT_HEIGHT)
win.setBackground('black')
t0=time.clock()
cou=0
life=Rectangle(Point(0,HEIGHT),Point(WIDTH,TOT_HEIGHT))
life.setFill('yellow')
life.draw(win)
for x in range(0,WIDTH,50):
    for y in range(0,HEIGHT,50):
        prob=random.randint(1,100)
        if(prob<=CHANCE):
            rec=Rectangle(Point(x,y),Point(x+50,y+50))
            rec.setFill('red')
            rec.draw(win)
            squares=squares+1
            walls.append((x+25,y+25))
        else:
            ex=random.randint(1,100)
            if(ex<=20 and exist==False):
                player=Circle(Point(x+25,y+25),25)
                player.setFill('yellow')
                player.draw(win)
                short=Circle(Point(x+45,y+25),5)
                short.setFill('green')
                short.draw(win)
                exist=True
#print((squares*100)/total)
for i in range(GUARD_NUM):
    while(True):
        x=random.randint(0,int((WIDTH-50)/50))
        y=random.randint(0,int((HEIGHT-50)/50))
        P=(x*50+25,y*50+25)
        if P not in walls:
            break
    cir=Circle(Point(x*50+25,y*50+25),25)
    cir.setFill('blue')
    cir.draw(win)
    guards.append(cir)
    gmove.append([0,0])
    gshot_exist.append(False)
    cir=Circle(Point(-1,-1),5)
    guard_shots.append(cir)
    gshot_dir.append([0,0])
    
xv,yv=PLAYER_MOVE,0
s1="Left"
while(True):
    t1=time.clock()
    if(t1-t0>=1):
        t0=t1
        cou=cou+1
        #print(3000-cou**2)
    
    s=win.checkKey()
    xval=0
    yval=0
    s1="ABS"
    correct=False
    if(s==None):
        continue
    if(s=="Up"):
        s1=s
        correct=True
        xval=0
        yval=(-1)*PLAYER_MOVE
        xv=xval
        yv=yval
    elif(s=="Down"):
        correct=True
        s1=s
        xval=0
        yval=PLAYER_MOVE
        xv=xval
        yv=yval
    elif(s=="Left"):
        s1=s
        correct=True
        xval=(-1)*PLAYER_MOVE
        yval=0
        xv=xval
        yv=yval
    elif(s=="Right"):
        s1=s
        correct=True
        xval=PLAYER_MOVE
        yval=0
        xv=xval
        yv=yval
    elif(s=='q'):
        s1="Left"
        correct=True
        xval=(-1)*PLAYER_MOVE
        yval=(-1)*PLAYER_MOVE
    elif(s=='e'):
        s1="Up"
        correct=True
        xval=PLAYER_MOVE
        yval=(-1)*PLAYER_MOVE
    elif(s=='z'):
        s1="Down"
        correct=True
        xval=(-1)*PLAYER_MOVE
        yval=PLAYER_MOVE
    elif(s=='c'):
        s1="Right"
        correct=True
        xval=PLAYER_MOVE
        yval=PLAYER_MOVE
    X,Y=player.getCenter().getX()+xval,player.getCenter().getY()+yval
    P=(X,Y)
    if P not in walls and (correct==True):
        if(X>0 and X<WIDTH and Y>0 and Y<HEIGHT):
            #
            #
            #
            #
            #print(gshot_dir)
            player.move(xval,yval)
    if(s1=="Left"):
        short.undraw()
        x,y=player.getCenter().getX(),player.getCenter().getY()
        short=Circle(Point(x-20,y),5)
        short.setFill('green')
        short.draw(win)
    elif(s1=="Up"):
        short.undraw()
        x,y=player.getCenter().getX(),player.getCenter().getY()
        short=Circle(Point(x,y-20),5)
        short.setFill('green')
        short.draw(win)
    elif(s1=="Right"):
        short.undraw()
        x,y=player.getCenter().getX(),player.getCenter().getY()
        short=Circle(Point(x+20,y),5)
        short.setFill('green')
        short.draw(win)
    elif(s1=="Down"):
        short.undraw()
        x,y=player.getCenter().getX(),player.getCenter().getY()
        short=Circle(Point(x,y+20),5)
        short.setFill('green')
        short.draw(win)
    if(s=='x'):
        #print(xv,yv)
        if(xv==0 or yv==0):
            X,Y=player.getCenter().getX(),player.getCenter().getY()
            ci=Circle(Point(X,Y),5)
            ci.setFill('white')
            ci.draw(win)
            player_shots.append(ci)
            pshot_dir.append([xv/PLAYER_MOVE*SHOT_SPEED,yv/PLAYER_MOVE*SHOT_SPEED])
    l=len(player_shots)
    flag=True
    gflag=True
    for i in range(l):
        #print(len(player_shots))
        if(flag==False):
            break
        X,Y=player_shots[i].getCenter().getX(),player_shots[i].getCenter().getY()
        P1=(X,Y-1)
        P2=(X,Y+1)
        P3=(X-1,Y)
        P4=(X+1,Y)
        P5=(X,Y)
        flag=False
        if (P1 not in walls) and (P2 not in walls) and (P3 not in walls) and (P4 not in walls) and (P5 not in walls):
            if(X>0 and X<WIDTH and Y>0 and Y<HEIGHT):
                player_shots[i].move(pshot_dir[i][0],pshot_dir[i][1])
                flag=True
        for j in range(len(guards)):
            dis=distance(guards[j].getCenter(),player_shots[i].getCenter())
            if(dis<=25):
                flag=False
                guards[j].undraw()
                del guards[j]
                del gmove[j]
                if(gshot_exist[j]==True):
                    guard_shots[j].undraw()
                    del guard_shots[j]
                    del gshot_dir[j]
                    del gshot_exist[j]
                if(len(guards)<=0):
                    you_win()
                break
        if(flag==False):
            player_shots[i].undraw()
            del player_shots[i]
            del pshot_dir[i]


    #From here, Guard movement

            
    for i in range(len(guards)):
        cen=guards[i].getCenter()
        X=cen.getX()
        Y=cen.getY()
        flag=False
        if((X-25)%50==0 and (Y-25)%50==0):
            while(True):
                while(True):
                    x=random.randint(0,2)
                    y=random.randint(0,2)
                    if(x==1 or y==1):
                        break
                X,Y=cen.getX(),cen.getY()
                X,Y=X+(options[x]*int(50/GUARD_MOVE)),Y+(options[y]*int(50/GUARD_MOVE))
                P=(X,Y)
                if P not in walls:
                    if(X>0 and X<WIDTH and Y>0 and Y<HEIGHT):
                        gmove[i][0],gmove[i][1]=options[x],options[y]
                        flag=True
                        
                if(flag==True):
                    break
        guards[i].move(gmove[i][0],gmove[i][1])

    for j in range(len(guards)):
        cen=guards[j].getCenter()
        gX=cen.getX()
        gY=cen.getY()
        pX,pY=player.getCenter().getX(),player.getCenter().getY()
        wallflag=False
        if(pX==gX):
            for k in range(int(min(pY,gY)),int(max(pY,gY))):
                P=(pX,k)
                if P in walls:
                    wallflag=True
                    break
            if(wallflag==False and gshot_exist[j]==False):
                cir=Circle(guards[j].getCenter(),5)
                cir.setFill('blue')
                cir.draw(win)
                guard_shots[j]=cir
                if(pY>gY):
                    gshot_dir[j]=[0,GUARD_SHOT]
                    gshot_exist[j]=True
                else:
                    gshot_dir[j]=[0,(-1)*GUARD_SHOT]
                    gshot_exist[j]=True
        if(pY==gY):
            for k in range(int(min(pX,gX)),int(max(pX,gX))):
                P=(k,pY)
                if P in walls:
                    wallflag=True
                    break
            if(wallflag==False and gshot_exist[j]==False):
                cir=Circle(guards[j].getCenter(),5)
                cir.setFill('blue')
                cir.draw(win)
                guard_shots[j]=cir
                if(pX>gX):
                    gshot_dir[j]=[GUARD_SHOT,0]
                    gshot_exist[j]=True
                else:
                    gshot_dir[j]=[(-1)*GUARD_SHOT,0]
                    gshot_exist[j]=True
    sflag=True
    valid=True
    for i in range(len(guard_shots)):
        #print(len(player_shots))
        #if(valid==False):
        #    break
        X,Y=guard_shots[i].getCenter().getX(),guard_shots[i].getCenter().getY()
        P1=(X,Y-1)
        P2=(X,Y+1)
        P3=(X-1,Y)
        P4=(X+1,Y)
        P5=(X,Y)
        P6=(X,Y-2)
        P7=(X,Y+2)
        P8=(X-2,Y)
        P9=(X+2,Y)
        P10=(X,Y-3)
        P11=(X,Y+3)
        P12=(X-3,Y)
        P13=(X+3,Y)
        sflag=True
        valid=True
        if (P1 not in walls) and (P2 not in walls) and (P3 not in walls) and (P4 not in walls) and (P5 not in walls) and (P6 not in walls) and (P7 not in walls) and (P8 not in walls) and (P9 not in walls) and (P10 not in walls) and (P11 not in walls) and (P12 not in walls) and (P13 not in walls):
            if(gshot_exist[i]==True):
                if(X>0 and X<WIDTH and Y>0 and Y<HEIGHT):
                    guard_shots[i].move(gshot_dir[i][0],gshot_dir[i][1])
                    sflag=False
                else:
                    valid=False
            else:
                valid=True
        else:
            valid=False
        if(valid==False):
            guard_shots[i].undraw()
            gshot_exist[i]=False
            gshot_dir[i]=[0,0]
    for i in range(len(guard_shots)):
        dis=distance(player.getCenter(),guard_shots[i].getCenter())
        if(dis<25 and gshot_exist[i]==True):
            #print(span,howlong)
            l=Line(Point(span-howlong,TOT_HEIGHT-int((TOT_HEIGHT-HEIGHT)/2)),Point(span,TOT_HEIGHT-int((TOT_HEIGHT-HEIGHT)/2)))
            l.setWidth(TOT_HEIGHT-HEIGHT)
            l.setFill('black')
            l.draw(win)
            span=span-howlong
            guard_shots[i].undraw()
            gshot_exist[i]=False
            gshot_dir[i]=[0,0]
            if(span<=0):
                you_lose()
    #print("break")
    time.sleep(0.01)
