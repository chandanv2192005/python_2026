# Simple Class (OOP) Demo
# Classes are like "blueprints" for creating objects.

class Robot:
    # The __init__ method is a constructor (runs when you create a new robot)
    def __init__(self, name, model, battery_level=100):
        self.name = name
        self.model = model
        self.battery = battery_level

    # A custom method
    def introduce(self):
        print(f"Hello! I am {self.name}, a {self.model} model. Battery: {self.battery}%")

    def charge(self):
        self.battery = 100
        print(f"{self.name} is now fully charged!")

def main():
    # Create two different robot "objects" from the same "blueprint"
    bot1 = Robot("R2-D2", "Astromech")
    bot2 = Robot("C-3PO", "Protocol", battery_level=45)

    # Use the objects
    bot1.introduce()
    bot2.introduce()

    print("\nExecuting action...")
    bot2.charge()
    bot2.introduce()

if __name__ == "__main__":
    main()
