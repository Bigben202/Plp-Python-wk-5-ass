# Question 1
class Superhero:
    def __init__(self, name, alias, power, origin):
        self._name = name              # Encapsulated (private) attribute
        self.alias = alias
        self.power = power
        self.origin = origin

    def use_power(self):
        return f"{self.alias} uses {self.power}!"

    def get_identity(self):
        return f"{self.alias}'s true identity is {self._name} from {self.origin}."

# Subclass: FlyingHero
class FlyingHero(Superhero):
    def __init__(self, name, alias, origin, flight_speed):
        super().__init__(name, alias, "Flight", origin)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.alias} takes off into the sky at {self.flight_speed} mph!"

# Subclass: TechHero
class TechHero(Superhero):
    def __init__(self, name, alias, origin, gadget):
        super().__init__(name, alias, "Advanced Technology", origin)
        self.gadget = gadget

    def use_power(self):
        return f"{self.alias} deploys their {self.gadget} with high precision!"


# Testing our classes
if __name__ == "__main__":
    hero1 = FlyingHero("Clark Kent", "SuperFly", "Krypton", 1200)
    hero2 = TechHero("Tony Stark", "IronMind", "Earth", "Nano Suit")

    print(hero1.get_identity())
    print(hero1.use_power())
    print(hero2.get_identity())
    print(hero2.use_power())

# Question 2
# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement move()")


# Subclass: Car
class Car(Vehicle):
    def move(self):
        return f"{self.name} is Driving on the road! 🚗"


# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is Flying through the sky! ✈️"


# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return f"{self.name} is Sailing across the sea! 🚢"


# Subclass: Train
class Train(Vehicle):
    def move(self):
        return f"{self.name} is Zooming along the tracks! 🚄"


# Function to demonstrate polymorphism
def test_vehicles_movement(vehicles):
    for vehicle in vehicles:
        print(vehicle.move())


# Example usage
if __name__ == "__main__":
    car = Car("Mustang")
    plane = Plane("Boeing 747")
    boat = Boat("Sea Breeze")
    train = Train("Bullet Express")

    vehicle_list = [car, plane, boat, train]
    test_vehicles_movement(vehicle_list)
