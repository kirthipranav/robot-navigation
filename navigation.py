
Conversation opened. 1 read message.

Skip to content
Using Gmail with screen readers
robot navigation 

18 of many
CODE
Inbox

Kirthi Pranav Murali Krishnan <kirthipranav11@gmail.com>
Attachments
Mar 19, 2022, 10:10 AM
to me


 3 Attachments
  •  Scanned by Gmail
robot navigation source issues
from re import I
import turtle
from Utility import Point
from Utility import Line
import Utility

r1 = Point(0,0)
paths = []
navigate = []
mn = 30
turtle.speed(1000)
boundarywidth = 600
boundaryheight = 600

boundary_width = boundarywidth/2
boundary_height = boundaryheight/2
boundary_width_scaled_down = boundary_width / mn
boundary_height_scaled_down = boundary_height / mn

def isBetween (A, B,C):
    Mi = min (B,C)
    Ma = max (B,C)
    return(Mi <= A <= Ma)

def pathfind(x1,y1,x2,y2,x3,y3,path_name):
    x4 = x1-x2
    y4 = y1-y2
 
    ip1 = Point(0,0)
    #Vertical Line
    if x4 == 0:
        if isBetween(y3,y1,y2):
            x = x1
            y = y3
        elif y3 > y2:
            x = x2
            y = y2
        else:
            x = x1
            y = y1
        print("{} is a vertical line and the intercept is at: ({},{})".format(path_name.strip(),x,y))
        ip1.x = x
        ip1.y = y
        return(ip1)
    
    #Horizontal Line
    elif y4 == 0:
        if isBetween(x3,x1,x2):
            y = y1
            x = x3
        elif x3 < x1:
            y = y1
            x = x1
        else:
            y = y2
            x = x2
        print("{} is a horizontal line and the intercept is at: ({},{})".format(path_name.strip(),x,y))
        ip1.x = x
        ip1.y = y
        return(ip1)
    else:
        #Slope of the line
        m1 = y4/x4
        p1 = m1*x1
        c1 = y1-p1
        p2 = (-1/m1)*x3
        c2 = y3-p2
        x = ((c2-c1)*m1)/(m1**2+1)
        y = (m1*x)+c1
        ip1.x = x
        ip1.y = y
        print("{} is a diagonal line and the intercept is at: ({},{})".format(path_name.strip(),x,y))
        return(ip1)

def drawBoundary():
    turtle.pensize(8)
    turtle.penup()
    turtle.goto(boundary_width,boundary_height)
    turtle.pencolor("red")
    turtle.pendown()
    turtle.goto(boundary_width,-boundary_height)
    turtle.goto(-boundary_width,-boundary_height)
    turtle.goto(-boundary_width,boundary_height)
    turtle.goto(boundary_width,boundary_height)
    turtle.penup()
    turtle.pensize(10)
    turtle.pencolor("green")
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(0,0)
    turtle.pensize(1)
    turtle.goto(boundary_height,0)
    turtle.goto(-boundary_height,0)
    turtle.penup()
    turtle.goto(0,boundary_width)
    turtle.pendown()
    turtle.goto(0,-boundary_width)
    turtle.pencolor("black")
    turtle.penup()
    turtle.pensize(2)

def robot():
    robotx,roboty = input("Type the current location of the robot: ").split(",")
    r1.x = int(robotx)
    r1.y = int(roboty)
    r1.name = "Robot Location"

    if r1.x > boundary_width_scaled_down:
        r1.x = boundary_width_scaled_down
    elif r1.x < -boundary_width_scaled_down:
        r1.x = -boundary_width_scaled_down
    
    if r1.y > boundary_height_scaled_down:
        r1.y = boundary_height_scaled_down
    elif r1.y < -boundary_height_scaled_down:
        r1.y = -boundary_height_scaled_down
    
    turtle.goto(r1.x,r1.y)
    turtle.penup()
    turtle.pencolor("black")
    for path in paths:
        intercept(r1,path)
    
def intercept(r1,path):
    interceptpoint = pathfind(path.startpoint.x,path.startpoint.y,path.endpoint.x,path.endpoint.y,r1.x,r1.y,path.name)
    path.setIntercept(interceptpoint,r1)

def sortPath():
    sorted_paths = Utility.sortmypath(paths)
    for sorted_path in sorted_paths:
        print("{}'s intercept distance is: {}".format(sorted_path.name.strip(),sorted_path.interceptdistance))
    return(sorted_paths)

def createPath():
    f_lines = []
    with open('C:\\Users\\Kirth\\OneDrive\\Documents\\Kirthi\\Code\\Layout.txt') as f:
        f_lines = f.readlines()
        for f_line in f_lines:
            l1 = Line()
            line = f_line.split(",")
            l1.startpoint.x = int (line[0])
            l1.startpoint.y = int (line[1])
            l1.endpoint.x = int (line[2])
            l1.endpoint.y = int (line[3])
            l1.name = line[4].strip()

            if l1.startpoint.x > boundary_width_scaled_down:
                l1.startpoint.x = boundary_width_scaled_down
            elif l1.startpoint.x < -boundary_width_scaled_down:
                l1.startpoint.x = -boundary_width_scaled_down

            if l1.endpoint.x > boundary_width_scaled_down:
                l1.endpoint.x = boundary_width_scaled_down
            elif l1.endpoint.x < -boundary_width_scaled_down:
                l1.endpoint.x = -boundary_width_scaled_down

            if l1.startpoint.y > boundary_height_scaled_down:
                l1.startpoint.y = boundary_height_scaled_down
            elif l1.startpoint.y < -boundary_height_scaled_down:
                l1.startpoint.y = -boundary_height_scaled_down

            if l1.endpoint.y > boundary_height_scaled_down:
                l1.endpoint.y = boundary_height_scaled_down
            elif l1.endpoint.y < -boundary_height_scaled_down:
                l1.endpoint.y = -boundary_height_scaled_down
            turtle.penup()
            turtle.goto(l1.startpoint.x*mn, l1.startpoint.y*mn)
            turtle.pendown()
            turtle.goto(l1.endpoint.x*mn, l1.endpoint.y*mn)
            turtle.write(l1.name)
            turtle.penup()
            paths.append(l1)

def goClosestPath(sorted_paths):
    shortestpath = sorted_paths[0]
    turtle.penup()
    turtle.goto(r1.x*mn,r1.y*mn)
    turtle.pencolor("orange")
    turtle.pendown()
    turtle.goto(shortestpath.interceptpoint.x*mn,shortestpath.interceptpoint.y*mn)

def connectPath():
    for p in paths:
        for path in paths:
            if not Utility.isSameLine(p,path) and \
                Utility.doIntersect(p.startpoint,p.endpoint,path.startpoint,path.endpoint) and \
                    not Utility.checkIfPathExistInPath(p,path):
                        p.next.append(path)
    for path in paths:
        for i in path.next:
            print("{} ---> {}".format(path.name,i.name))

def navigateDestination(s1,where_name):
    turtle.goto(s1.endpoint.x*mn,s1.endpoint.y*mn)
    for s in s1.next:
        if not s.name == where_name:
            navigateDestination(s,where_name)
            navigate.append(s1)
        else:
            print("Match found {},{}".format(s1.name,s.name))

drawBoundary()
createPath()
connectPath()
robot()
sorted_path = sortPath()
goClosestPath(sorted_path)
navigateDestination(sorted_path[0],"Kitchen")
for n in navigate:
    print(n.name)
turtle.done()
Navigation5 (2).txt
Displaying Navigation5 (2).txt.
