from random import random


class Animal:
    life_expectancies = {"panda": 100, "tiger": 30, "bear": 50}
    average_weight = {"panda": 100, "tiger": 300, "bear": 400}

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expectancy = 50
        if self.gender == "female":
            self.gestation_period = (self.age * 2) % 2
        self.chance_of_dying = self.age / self.life_expectancy
        for key in self.life_expectancies:
            if key == species:
                self.life_expectancy = self.life_expectancies[key]

    def grow(self, weight, years):
        self.weight += weight
        self.age += years

    def eat(self, weight):
        for key in self.average_weight:
            if key == self.species:
                self.weight += weight / 4
                if self.weight >= self.average_weight[key]:
                    self.weight = self.average_weight[key]
                    return self.weight
                else:
                    return self.weight

    def die(self):
        chance = random()
        return self.chance_of_dying > chance
