class Animal:
    def __init__(self, name="joe"):
        self.name = name
        self.sound = "moo"

    def speak(self):
        print(self.sound)
    def get_name(self):
        print(self.name)