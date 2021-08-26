def end(lose):
    global minutes
    global seconds
    global ti
    ti.undraw()
    if(lose==True):
        dec="You LOSE"
    else:
        dec="You WIN"
    if(minutes<10):
        f="0"+str(minutes)
    else:
        f=str(minutes)
    f=dec+"    Time taken: "+f
    m=":"
    if(seconds<10):
        l="0"+str(seconds)
    else:
        l=str(seconds)
    fin=f+m+l
    ti=Text(Point(int((SIZE-YLOW)/2),int(YLOW/2)),fin)
    ti.setSize(30)
    #ti.setStyle('bold')
    ti.setTextColor('white')
    ti.draw(win)

def update_time():
    global minutes
    global seconds
    global ti
    ti.undraw()
    seconds=seconds+1
    if(seconds==60):
        minutes=minutes+1
        seconds=0
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
    ti=Text(Point(int((SIZE-YLOW)/2),int(YLOW/2)),fin)
    ti.setSize(30)
    ti.setStyle('bold')
    ti.setTextColor('white')
    ti.draw(win)

def deleteye():
    global yellow
    if(len(yellow)==0):
        return
    x=yellow[len(yellow)-1][0]
    y=yellow[len(yellow)-1][1]
    re=Rectangle(Point(x-int(SQUARE_SIZE/2),y-int(SQUARE_SIZE/2)),Point(x+int(SQUARE_SIZE/2),y+int(SQUARE_SIZE/2)))
    re.setFill('red')
    re.draw(win)
    del yellow[len(yellow)-1]

def draw_number(x,y,direct):
    global MINE_NUM
    global mine_grid
    global SQUARE_SIZE
    global YLOW
    global clicks
    global exposed
    global yellow
    global enum
    i,j=y,x
    #print(i,j)
    if(x<0 or x>=MINE_NUM or y<0 or y>=MINE_NUM):
        #print(i,j)
        return
    if(direct==True and clicks[i][j]==0):
        rec=Rectangle(Point(x*SQUARE_SIZE,y*SQUARE_SIZE+YLOW),Point((x+1)*SQUARE_SIZE,(y+1)*SQUARE_SIZE+YLOW))
        rec.setFill('yellow')
        rec.draw(win)
        clicks[i][j]=clicks[i][j]+1
        ###############################################
        yellow.append([x*SQUARE_SIZE+int(SQUARE_SIZE/2),y*SQUARE_SIZE+YLOW+int(SQUARE_SIZE/2)])
    elif(direct==True and clicks[i][j]==1):
        rec=Rectangle(Point(x*SQUARE_SIZE,y*SQUARE_SIZE+YLOW),Point((x+1)*SQUARE_SIZE,(y+1)*SQUARE_SIZE+YLOW))
        rec.setFill('black')
        rec.draw(win)
        yellow.remove([x*SQUARE_SIZE+int(SQUARE_SIZE/2),y*SQUARE_SIZE+YLOW+int(SQUARE_SIZE/2)])
        clicks[i][j]=clicks[i][j]+1
        if(mine_grid[i][j]==0):
            f=" "
        else:
            f=str(mine_grid[i][j])
        txt=Text(Point(x*SQUARE_SIZE+int(SQUARE_SIZE/2),y*SQUARE_SIZE+YLOW+int(SQUARE_SIZE/2)),f)
        txt.setSize(TEXT_SIZE)
        txt.setTextColor('white')
        txt.draw(win)
        clicks[i][j]=clicks[i][j]+1
        exposed[i][j]=True
        enum=enum-1
        if(mine_grid[i][j]==0):
            draw_number(x-1,y,False)
            draw_number(x+1,y,False)
            draw_number(x,y-1,False)
            draw_number(x,y+1,False)
    if(direct==False and exposed[i][j]==False):
        if(mine_grid[i][j]<0):
            return
        rec=Rectangle(Point(x*SQUARE_SIZE,y*SQUARE_SIZE+YLOW),Point((x+1)*SQUARE_SIZE,(y+1)*SQUARE_SIZE+YLOW))
        rec.setFill('black')
        rec.draw(win)
        if(mine_grid[i][j]==0):
            f=" "
        else:
            f=str(mine_grid[i][j])
        txt=Text(Point(x*SQUARE_SIZE+int(SQUARE_SIZE/2),y*SQUARE_SIZE+YLOW+int(SQUARE_SIZE/2)),f)
        txt.setSize(TEXT_SIZE)
        txt.setTextColor('white')
        txt.draw(win)
        exposed[i][j]=True
        enum=enum-1
        if(mine_grid[i][j]==0):
            draw_number(x-1,y,False)
            draw_number(x+1,y,False)
            draw_number(x,y-1,False)
            draw_number(x,y+1,False)
        else:
            return

from graphics import *
import random
import math

SIZE=650
YLOW=50
MINE_NUM=10
SQUARE_SIZE=int((SIZE-YLOW)/MINE_NUM)
TEXT_SIZE=30

mines=[]
mine_grid=[]
exposed=[]
clicks=[]
yellow=[]
enum=MINE_NUM**2
lose=False

for i in range(MINE_NUM):
    mine_grid.append([])
    exposed.append([])
    clicks.append([])
    for j in range(MINE_NUM):
        mine_grid[i].append(0)
        exposed[i].append(False)
        clicks[i].append(0)
win=GraphWin("Minesweeper",SIZE-YLOW,SIZE)
win.setBackground('black')
i=0
col=['white','violet','indigo','blue','green','yellow','orange','red','brown','gray']
while(True):
    x=random.randint(1,MINE_NUM-1)*SQUARE_SIZE+int(SQUARE_SIZE/2)
    y=random.randint(1,MINE_NUM-1)*SQUARE_SIZE+int(SQUARE_SIZE/2)+YLOW
    P=[x,y]
    if P not in mines:
        mines.append([x,y])
        #cir=Circle(Point(x,y),10)
        #cir.setFill(col[i])
        #cir.draw(win)
        x=int((x-int(SQUARE_SIZE/2))/SQUARE_SIZE)
        y=int((y-YLOW-int(SQUARE_SIZE/2))/SQUARE_SIZE)
        mine_grid[x][y]=-1
        i=i+1
    if(i==MINE_NUM):
        break
for i in range(MINE_NUM):
    for j in range(MINE_NUM):
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if(x==i and y==j):
                    continue
                if(x>=0 and x<MINE_NUM and y>=0 and y<MINE_NUM):
                    try:
                        if(mine_grid[i][j]<0 and mine_grid[x][y]>=0):
                            mine_grid[x][y]=mine_grid[x][y]+1
                    except IndexError:
                        print(i,j,x,y)
for i in range(YLOW,SIZE,SQUARE_SIZE):
    for j in range(0,SIZE,SQUARE_SIZE):
        re=Rectangle(Point(j,i),Point(j+SQUARE_SIZE,i+SQUARE_SIZE))
        re.setFill('red')
        re.draw(win)
#for i in range(0,MINE_NUM):
#    for j in range(0,MINE_NUM):
#        txt=Text(Point(j*SQUARE_SIZE+int(SQUARE_SIZE/2),i*SQUARE_SIZE+int(SQUARE_SIZE/2)+YLOW),str(mine_grid[i][j]))
#        txt.setSize(TEXT_SIZE)
#        txt.setTextColor('white')
#        txt.draw(win)
#print(mine_grid)
t0=time.clock()
count=0
minutes,seconds=0,0
ti=Text(Point(0,0),"txt")
ti.draw(win)
update_time()
mine=[]
for i in range(MINE_NUM):
    for j in range(MINE_NUM):
        if(mine_grid[i][j]<0):
            mine.append([j*SQUARE_SIZE+int(SQUARE_SIZE/2),i*SQUARE_SIZE+int(SQUARE_SIZE/2)+YLOW])
#print(exposed)
while(True):
    t1=time.clock()
    if(t1-t0>=1):
        update_time()
        t0=t1
    p=win.checkMouse()
    if(p==None):
        continue
    Y=int(p.getX()/SQUARE_SIZE)
    X=int((p.getY()-YLOW)/SQUARE_SIZE)
    if(p.getY()<YLOW):
        deleteye()
        continue
    #print(X,Y)
    if(exposed[X][Y]==True):
        continue
    if(mine_grid[X][Y]<0 and clicks[X][Y]==1):
        lose=True
        break
    draw_number(Y,X,True)
    if(enum==MINE_NUM):
        #print("You WIN")
        break
    if(sorted(mine)==sorted(yellow)):#set(yellow)==set(mine)):
        #print("You win")
        break
for i in range(MINE_NUM):
    for j in range(MINE_NUM):
        if(mine_grid[i][j]<0):
            cir=Circle(Point(j*SQUARE_SIZE+int(SQUARE_SIZE/2),i*SQUARE_SIZE+int(SQUARE_SIZE/2)+YLOW),int(SQUARE_SIZE/2))
            if(lose==True):
                cir.setFill('blue')
            else:
                cir.setFill('green')
            cir.draw(win)
end(lose)
