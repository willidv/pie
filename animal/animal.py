class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    
    def walk(self):
        self.health -= 5
        return self

    def run(self):
        self.health -= 10
        return self
# Animal1 = Animal("Ginger", 100)
# Animal1.walk().walk().walk()
# print Animal1.health

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150
    def pet(self):
        self.health += 5
# Dog1 = Dog("Ginny", 150)
# Dog1.walk().walk().walk().run().pet()
# print Dog1.health


class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon, self).__init__(name, health)
        self.health = 170
    def fly(self):
        self.health += 10
        return self
    def display_health(self):
        print "I am a Dragon, health is " + str(self.health)

Dragon1 = Dragon("Vgym", 170)
Dragon1.walk().walk().run().fly().display_health()
