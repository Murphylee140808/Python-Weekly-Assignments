# Activity 2: Polymorphism Example with Vehicles

class Vehicle:
    def move(self):
        return "This vehicle moves in some way."

class Car(Vehicle):
    def move(self):
        return "Driving"

class Plane(Vehicle):
    def move(self):
        return "Flying"

class Boat(Vehicle):
    def move(self):
        return "Sailing"


# Usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
