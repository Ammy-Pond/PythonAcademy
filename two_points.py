import math  
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist=round(dist,2)
    print(dist)
    return dist  

distance(10,2,4,5)