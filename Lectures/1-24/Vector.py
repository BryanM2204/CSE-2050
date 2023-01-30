class Vector:
    #constructr method
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #instance variables

    def magntitude(self):
        return (self.x**2 + self.y**2)**(1/2)

    def __repr__(self):
        return f"Vector: {self.x}, {self.y}"

my_list = list()
v1 = Vector()