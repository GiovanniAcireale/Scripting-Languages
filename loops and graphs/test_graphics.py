from graphics import *
import math
import random

win = GraphWin('Golden Angle', 1920,1080)

win.setBackground("black")

# Try adding text <---
titlePt = Point(300, 125)
title = Text(titlePt, "Golden Angle on a Graph")
title.setFace('times roman')
title.setSize(24)
title.setStyle('bold italic')
title.setTextColor("gold")
title.draw(win)

subPt = Point(300, 150)
sub = Text(subPt, "(represented by 500 points on a graph)")
sub.setFace('times roman')
sub.setSize(12)
sub.setStyle('normal')
sub.setTextColor("gold")
sub.draw(win)



def drawGold(t, angle = 137.508, size = 25, cspread = 20):
    # t = amount of points
    
    phi = angle * ( math.pi / 180.0 )
    xcenter = 960.0
    ycenter = 540.0
   
    for n in range (0,t):
        r = cspread * math.sqrt(n)
        theta = n * phi
        
        x = r * math.cos(theta) + xcenter
        y = r * math.sin(theta) + ycenter
        
        # Experiment with random colors <---
        # Experiment with making custom colors <---
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = color_rgb(r, g, b)

        # Use rectangles or triangles instead of circles <---
        p1 = Point(x, y)
        p2 = Point(x + size/2, y + size)
        p3 = Point(x - size/2, y + size)
        triangle = Polygon(p1, p2, p3)
        triangle.setOutline("gold")
        triangle.setFill("gold")
        
        triangle.draw(win)
    
drawGold(500)

win.getMouse()
