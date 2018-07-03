from Animal import Animal


class Pig(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.sound = "oink"
    def speak(self):
        print("pigs always say", self.sound)