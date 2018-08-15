import math

class Point():
    '''creating class Point'''
    pass

    def __init__(self, x1, y1, x2, y2):
        '''initializing self variable'''
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        '''calculating distance between (x1, y1) and (x2, y2)'''
        sq1 = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
        print(sq1)

p = Point(1,4,5,8)
'''inputing values for point variables'''
p.distance()




# Point.distance(p) where p is another point that returns a floating point
# value for the distance between the two points
# if one point is (x1, y1) and another point is (x2, y2) then the formula
# for distance is 
# math.sqrt((x1 - x2) `**` 2 + (y1 - y2) `**` 2)

# p = Point(0,0)
# p.display()