class Person:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

    def credentials(self):
        return f"Person: '{self.name}' w/ netid '{self.ID}'"

    def __repr__(self):
        return f"Person: {self.name} w/ netid {self.ID}"


class Employee(Person):
    def __init__(self, name, netid, office):
        Person.__init__(self, name, netid)
        self.office = office

        #Method 2
        # super().__init__(name, netid)
        # self.office = office

        #Mehod 3: DONT USE
        # self.name = name
        # self.netid = netid
        # self.office = office

    def assign_office(self, office):
        self.office = office

# class Shape:
#     #defines stuff

# class Circle(Shape): #Inheritance - a circile is a shape

name = input()
person_ID = input()
p1 = Person(name, person_ID)
print(p1)