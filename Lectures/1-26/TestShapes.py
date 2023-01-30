from Shapes import Point
import unittest

class TestPoint(unittest.TestCase):
    'test cases for class Point'
    def setUp(self):
        self.p1 = Point(3, 4)
        self.p2 = Point(3, 4)
        self.p3 = Point(5, 6)

    def test_init(self):
        self.assertEqual(self.p1, 3)
        self.assertEqual(self.p1, 4)

    def test_eq(self):
        self.assertEqual(self.p1, self.p2)
        self.assertNotEqual(self.p1, self.p3)

    def test_distance(self):
    #D.R.Y = dont repeaet yourself
        self.assertEqual(self.p1.distance(self.p2), 0)
        self.assertAlmostEqual(self.p1.distance(self.p3), 2.828) #sqrt(2) = 1.414

class TestRectangle(unittest.TestCase):
    def test_init(self):
        p1 = Point(0, 0)
        p2 = Point(0, 1)
        p3 = Point(1, 1)
        p4 = Point(1, 0)
        
        points = [p1, p2, p3, p4]
        r1 = Rectangle(points)

    
    #develop a rectangle class
    #use composition - a rectangle has 4 points
    #define a method Rectangle.perimeter()

unittest.main() #runs all tests above