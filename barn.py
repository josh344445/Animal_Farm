from Animal import Animal
from Horse import Horse
from Pig import Pig
if __name__ == "__main__":
    cow = Animal()
    cow.speak()
    horse = Horse("Bill")
    horse.speak()

    horse2 = Horse("billy")
    horse.get_name()
    horse2.get_name()
    pig=Pig
    pig.name="jon"
    pig.speak()