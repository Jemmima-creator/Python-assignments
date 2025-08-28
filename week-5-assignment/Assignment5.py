# ---------------- Assignment 1 ----------------
# Design Your Own Class

# A  class representing a Pet
class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def introduce(self):
        print(f"This is {self.name}, a {self.age}-year-old {self.species}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")


# A subclass (Dog) showing inheritance
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, "Dog", age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof woof!")


# Example usage of Assignment 1
print("Assignment 1 Output:")
my_pet = Pet("Coco", "Parrot", 2)
my_pet.introduce()
my_pet.celebrate_birthday()

dog = Dog("Buddy", 3, "Golden Retriever")
dog.introduce()
dog.bark()


# ---------------- Assignment 2 ----------------
# Polymorphism Challenge

class Car:
    def move(self):
        print("The car is driving on the road.")

class Boat:
    def move(self):
        print("The boat is sailing on the water.")

class Plane:
    def move(self):
        print("The plane is flying in the air.")

# Example usage of Assignment 2
print("\nAssignment 2 Output:")
vehicles = [Car(), Boat(), Plane()]

for vehicle in vehicles:
    vehicle.move()
