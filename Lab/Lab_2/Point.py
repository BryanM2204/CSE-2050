class Point:
    """
    The class Point has and x and y value passed through it to do comparisons with other points using comparators which are then used in assertion tests that return True or False. It can also return a string of the point that is passed 
    __init__ initializes an x and y variable
    dist_from_origin calculates the distance of each point from the origin
    __gt__ calculates if the distance of the first point is greater than the second point
    __lt__ calculates if the distance of the first point is lesser than the second point
    __eq__ calculates if the distances are equal
    __str__ returns a string containing a point that is passed through the class
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def dist_from_origin(self):
        distance = (self.x**2 + self.y**2)**(1/2)
        return distance

    def __gt__(self, other):
        return self.dist_from_origin() > other.dist_from_origin()
        
    def __lt__(self, other):
        return self.dist_from_origin() < other.dist_from_origin()
    
    def __eq__(self, other):
        return self.dist_from_origin() == other.dist_from_origin()

    def __str__(self):
        return f'Point({self.x}, {self.y})'
        

if __name__ == '__main__':
    p1 = Point(3, 4)
    p2 = Point(3, 8)
    p3 = Point(11, 5)
    p4 = Point(0, 1)
    p5 = Point(5, 6)
    p6 = Point(5, 6)
    p7 = Point(0, 2)

    s = str(p1)
    print(s)

    assert p1.x == 3 #Expected True
    assert p1.y == 4 #Expected True

    assert p1 < p2  #Expected True
    assert not (p1 < p2) #Expected False

    assert p3 > p5 #Expected True
    assert not (p4 > p3) #Expected False

    assert p5 == p6 #Expected True
    assert not (p5 == p1) #Expected True

    assert str(p3) == 'Point (11, 5)'

    assert p7.dist_from_origin() == 2.0 #Expected True