from animals import Animal
from random import random


class Zoo:
    MONEY_PER_ANIMAL = 60
    DAYS_IN_MONTH = 30

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget
        self.foods = {"meat": 4, "grass": 2}

    def accomodate_new_animal(self, animal):
        if self.capacity == len(self.animals):
            raise ValueError("The capacity is full")
        for zoo_animal in self.animals:
            if zoo_animal.species == animal.species and zoo_animal.name == animal.name:
                raise ValueError("There is an animal with the same name")
        self.animals.append(animal)

    def daily_income(self):
        return self.MONEY_PER_ANIMAL * len(self.animals)
        self.budget += self.DAYS_IN_MONTH * self.MONEY_PER_ANIMAL * len(self.animals)

    def daily_outcome(self):
        outcome = 0
        for animal in self.animals:
            animal.eat()
            eaten_food = self.weight * self.food_weight_ratio
            outcome += eaten_food
            if animal.food_type == "carnivore":
                self.budget -= eaten_food * self.foods["meat"]
            else:
                self.budget -= eaten_food * self.foods["grass"]
        return outcome

    def die(self, animal1):
        if animal1.die():
            self.animals.remove(animal1)
            return True
        return False

    def newborn(self, parent1, parent2, name):
        chance_gender = random()
        if chance_gender > 0.5:
            gender = "male"
        else:
            gender = "female"
        newborn = Animal(parent1.species, 0, None, gender, 4)
        self.give_name_to_newborn(name)
        self.animals.append(newborn)

    def give_name_to_newborn(self, name):
        self.name = name

    def reproduce(self, animal1, animal2, name):
        same_gender = animal1.gender == animal2.gender
        same_species = animal1.species == animal2.species
        if animal1.gender == "female":
            female = animal1
        if animal2.gender == "female":
            female = animal2
        female_ready_to_reproduce = female.age >= 6 + female.start_pregnancy
        if not same_gender and same_species and female_ready_to_reproduce:
                self.newborn(animal1, animal2)
                female.start_pregnancy = female.age
