import json

class Player():
    def __init__(self, energy, health, fat, upper, lower, cardio):
        self.energy = energy
        self.health = health
        self.fat = fat
        self.upper = upper
        self.lower = lower
        self.cardio = cardio

    def save(self, slot):

        filename = f"save{slot}.json"
        data = {
            "energy": self.energy,
            "health": self.health,
            "fat": self.fat,
            "upper": self.upper,
            "lower": self.lower,
            "cardio": self.cardio
        }

        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Game Saved")

    @classmethod
    def load(cls, slot):
        filename = f"save{slot}.json"
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            print("Game loaded")
            return cls(
                data["energy"],
                data["health"],
                data["fat"],
                data["upper"],
                data["lower"],
                data["cardio"]
            )
        except FileNotFoundError:
            print("No save file found")
            return None
        
    def clamp(self):
        self.energy = max(0, min(self.energy, 100))
        self.fat = max(0, min(self.fat, 100))
        self.health = max(0, min(self.health, 100))
        self.upper = max(0, min(self.upper, 100))
        self.lower = max(0, min(self.lower, 100))
        self.cardio = max(0, min(self.cardio, 100))

    def get_status(self):
        print("Health: {}".format(self.health))
        print("Energy: {}".format(self.energy))
        print("Fat: {}".format(self.fat))
        print("Upper: {}".format(self.upper))
        print("Lower: {}".format(self.lower))

    

    def workout(self):
        self.clamp()
        print("1.- Upper Body")
        print("2.- Lower Body")
        print("3.- Cardio")
        decision = int(input("What would you like to work out? "))

        if decision == 1:
            self.fat -= 3
            self.energy -= 30
            self.upper += 5
            print("You did Upper, stats are: ")
            print(self.get_status())
        elif decision == 2:
            self.fat -= 3
            self.energy -= 40
            self.lower += 5
            print("You did Lower, stats are: ")
            print(self.get_status())
        elif decision == 3:
            self.health += 5
            self.energy -= 50
            self.fat -= 50
            self.cardio += 7
            print("You did Cardio, stats are: ")
            print(self.get_status())
        else:
            print("You didnt pick anything, douchbag")
        
    
    def get_food(self):
        self.clamp()
        print("Would you prefer: ")
        print("1.- Healthy Snack")
        print("2.- Bulky Snack")
        decisions = int(input("Pick by the number: "))

        if decisions == 1:
            self.energy += 20
            self.health += 15
            self.fat += 15
            print("You had a healthy Snack")

        elif decisions == 2:
            self.energy += 90
            self.health -= 5
            self.fat += 50
            self.cardio -= 5
            print("You had bulky meal")

        else:
            print("didnt pick anything,douchbag.")
        
        print("Had a feast, new stats are: ")
        self.get_status()

    #def __str__(self):

        


a1 = Player(100, 100, 20, 0, 0, 0)


while True:

    if a1.energy <= 0:
        print("You almost died, went to the hospital and have 30 in energy. All gains are lost")
        a1.upper = 0
        a1.lower = 0
        a1.energy = 30
    if a1.health <= 0:
        print("You died, looser")
        break

    if a1.upper == 100:
        print("You have reached your upper goal")


    print("\n--- MENU ---")
    print("1.- Workout")
    print("2.- Eat")
    print("3.- Status")
    print("4.- Save Game")
    print("5.- Load Game")
    print("6.- Exit")
    decision = int(input("What would you like to do: "))

    if decision == 1:
        a1.workout()
    elif decision == 2:
        a1.get_food()
    elif decision == 3:
        a1.get_status()
    elif decision == 4:
        slot = int(input("Which slot (1-3) do you want to save to: "))
        a1.save(slot)
    elif decision == 5:
        slot = int(input("Which slot (1-3) do you want to laod to: "))
        loaded = Player.load(slot)
        if loaded:
            a1 = loaded
    elif decision == 6:
        print("Goodbye, quitter")
        print("Final Status: ")
        a1.get_status()
        break

    else:
        print("Didnt pick anything")
