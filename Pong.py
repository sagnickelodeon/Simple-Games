from graphics import *
win=GraphWin('Pong',1000,600)
ldown=Line(Point(450,595),Point(550,595))
lup=Line(Point(450,5),Point(550,5))
win.setBackground('black')
lup.setFill('red')
ldown.setFill('red')
lup.setWidth(10)
ldown.setWidth(10)
lup.draw(win)
ldown.draw(win)
cir=Circle(Point(500,300),10)
cir.setFill('blue')
cir.draw(win)
up=False
upscore=0
downscore=0
mesup=Text(Point(50,200),str(upscore))
mesup.setTextColor('white')
mesup.setSize(30)
mesup.setStyle('bold')
mesup.draw(win)
mesdown=Text(Point(50,370),str(downscore))
mesdown.setTextColor('white')
mesdown.setSize(30)
mesdown.setStyle('bold')
mesdown.draw(win)
xmove=3
ymove=3
while(True):
    cir.move(xmove,ymove)
    circent=cir.getCenter()
    if(circent.getX()>=990 or circent.getX()<=10):
        xmove=xmove*-1
    if(circent.getY()>=575 or circent.getY()<=25):
        if(up==False):
            downscore=downscore+1
            up=True
            mesdown.undraw()
            mesdown=Text(Point(50,370),str(downscore))
            mesdown.setTextColor('white')
            mesdown.setSize(30)
            mesdown.setStyle('bold')
            mesdown.draw(win)
        else:
            up=False
            upscore=upscore+1
            mesup.undraw()
            mesup=Text(Point(50,200),str(upscore))
            mesup.setTextColor('white')
            mesup.setSize(30)
            mesup.setStyle('bold')
            mesup.draw(win)
        ymove=ymove*-1
        continue
    if(up==False):
        linecent=ldown.getCenter()
        if(circent.getX()>linecent.getX() and linecent.getX()<950):
            ldown.move(5,0)
        elif(circent.getX()<linecent.getX() and linecent.getX()>50):
            ldown.move(-5,0)
    elif(up==True):
        linecent=lup.getCenter()
        if(circent.getX()>linecent.getX() and linecent.getX()<950):
            lup.move(5,0)
        elif(circent.getX()<linecent.getX() and linecent.getX()>50):
            lup.move(-5,0)
    time.sleep(0.001)
