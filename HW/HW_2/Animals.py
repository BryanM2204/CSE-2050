class Animal:
    """
    This class is the super class that all other classes derive from
    """
    def __init__(self, name):
        self.name = name

    def reply(self):
        return self.speak()

class Mammal(Animal):
    """
    This class derives from the Animal class the instance variables name and sound
    Has method called speak that returns a name and sound
    """
    def __init__(self, name, sound):
        Animal.__init__(self, name)
        self.sound = sound 
    def speak(self):
        return f'{self.name} says {self.sound}!'

class Cat(Mammal):
    """
    This class derives from Mammal and initilizes it to the instance variables defined in the previous class through inheritance
    Has a speak method to return the name and sound 
    """
    def __init__(self, name, sound='meow'):
        Mammal.__init__(self, name, sound)

    def speak(self):
        return f'{self.name} says {self.sound}!'

class Dog(Mammal):
    """
    This class derives from Mammal and initilizes it to the instance variables defined in the previous class through inheritance
    Has a speak method to return the name and sound 
    """
    def __init__(self, name, sound='woof'):
        Mammal.__init__(self, name, sound)

    def speak(self):
        return f'{self.name} says {self.sound}!'

class Primate(Mammal):
    """
    This class derives from Mammal and initilizes it to the instance variables defined in the previous class through inheritance
    Has a speak method to return the name and sound 
    """
    def __init__(self, name, sound='ahh ahh'):
        Mammal.__init__(self, name, sound)

    def speak(self):
        return f'{self.name} says {self.sound}!'

class ComputerScientist(Primate):
    """
    This class derives from Primate and has initilizes it to the instance variables defined in the Primate class through inheritance
    when ComputerScientist.speak() is called upon it will default to the method defined in Primate
    """
    def __init__(self, name):
        Primate.__init__(self, name, sound='Hello World')
