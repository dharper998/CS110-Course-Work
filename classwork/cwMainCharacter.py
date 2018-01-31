import random
class MainCharacter:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.str = 0
        self.speed = 0
        self.intel = 0
        for i in range(10):
            print("You have " + str(i) + " skill points remaining")
            userin = input("Choose an attribute to add a skill point to: ")
            if userin == "strength":
                self.str += 1
            elif userin == "speed":
                self.speed += 1
            elif userin == "intel":
                self.intel += 1

    def move(self, direction):
        if direction == "right":
            self.x += 1
        elif direction == "left":
            self.x -= 1
        elif direction == "forward":
            self.y -= 1
        elif direction == "backward":
            self.y += 1

    def fight(self, opponent):
        oppstren = random.randrange(10)
        oppspeed = random.randrange(10 - oppstren)
        oppintel = random.randrange(10 - oppstren - oppspeed)
        strdiff = self.stren - oppstren
        speeddiff = self.speed - oppspeed
        inteldiff = self.intel - oppintel
        if (strdiff + speeddiff + inteldiff) >= 0
            return True
        else:
            return False
