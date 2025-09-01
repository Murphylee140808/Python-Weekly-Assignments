# Assignment 1: Superhero Class with Encapsulation & Inheritance

class Superhero:
    def __init__(self, name, power, city):
        # Encapsulated attributes
        self.__name = name
        self.__power = power
        self.__city = city

    # Getters
    def get_name(self):
        return self.__name
    
    def get_power(self):
        return self.__power
    
    def get_city(self):
        return self.__city

    # A method that all superheroes share
    def introduce(self):
        return f"I am {self.__name}, protector of {self.__city}!"


# Inheritance + Polymorphism
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.__flight_speed = flight_speed

    def introduce(self):
        return f"I am {self.get_name()}, I fly over {self.get_city()} at {self.__flight_speed} km/h!"


class StrongHero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.__strength_level = strength_level

    def introduce(self):
        return f"I am {self.get_name()}, my strength level is {self.__strength_level} tons!"


# Usage
hero1 = FlyingHero("SkyMan", "Flight", "Metropolis", 900)
hero2 = StrongHero("Titan", "Super Strength", "Gotham", 200)

print(hero1.introduce())
print(hero2.introduce())
