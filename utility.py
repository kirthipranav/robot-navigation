import math
class Point:
    def __init__(self):
        self.name = ""
        self.x = 0
        self.y = 0
    def __init__(self,x,y):
        self.name = ""
        self.x = x
        self.y = y

class Line:
    def __init__(self):
        self.name = ""
        self.startpoint = Point(0,0)
        self.endpoint = Point(0,0)
        self.interceptpoint = Point(0,0)
        self.interceptdistance = 0
        self.next = []
        self.prev = []
    
    def setIntercept(self,p1,r1):
        self.interceptpoint.x = p1.x
        self.interceptpoint.y = p1.y
        self.interceptdistance = self.calculateDistance(p1,r1)
    
    def calculateDistance(self,p1,p2):
        if p1.x == p2.x:
            return(int(math.fabs(p1.y-p2.y)))
        elif p1.y == p2.y:
            return(int(math.fabs(p1.x-p2.x)))
        else:
            hyp_square = (p1.x-p2.x)**2 + (p1.y-p2.y)**2
            return(int(math.fabs(math.sqrt(hyp_square))))


def sortmypath(paths):
    sortedpaths = paths[:]
    sortedpaths.sort(key=lambda x: x.interceptdistance)
    return(sortedpaths)

def onSegment(p, q, r):
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))):
        return True
    return False
 
def orientation(p, q, r):
    # to find the orientation of an ordered triplet (p,q,r)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    # for details of below formula.
     
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if (val > 0):
         
        # Clockwise orientation
        return 1
    elif (val < 0):
         
        # Counterclockwise orientation
        return 2
    else:
         
        # Collinear orientation
        return 0

def checkIfPathExistInPath(p1,path):
    for p in path.next:
        if p1.name == p.name:
            return (True)
    return (False)

def isSameLine(l1,l2):
    if l1.startpoint.x == l2.startpoint.x and l1.startpoint.y == l2.startpoint.y and l1.endpoint.x == l2.endpoint.x and l1.endpoint.y == l2.endpoint.y:
        return(True)
    else:
        return(False)


# The main function that returns true if
# the line segment 'p1q1' and 'p2q2' intersect.
def doIntersect(p1,q1,p2,q2):
     
    # Find the 4 orientations required for
    # the general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
 
    # General case
    if ((o1 != o2) and (o3 != o4)):
        return True
 
    # Special Cases
 
    # p1 , q1 and p2 are collinear and p2 lies on segment p1q1
    if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
 
    # p1 , q1 and q2 are collinear and q2 lies on segment p1q1
    if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
 
    # p2 , q2 and p1 are collinear and p1 lies on segment p2q2
    if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
 
    # p2 , q2 and q1 are collinear and q1 lies on segment p2q2
    if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
 
    # If none of the cases
    return False
