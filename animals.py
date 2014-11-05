from random import random
import json


class Animal:
    json_data = open("database.json")
    species_database = json.load(json_data)

    def __init__(self, species, month, name, gender, weight):
        self.species = species
        self.age = month
        self.name = name
        self.gender = gender
        self.weight = weight
        for animal in self.species_database["animals"]:
            if animal["species"] == species:
                self.life_expectancy = animal["life_expectancy"]
                self.food_type = animal["food_type"]
                self.gestation_period = animal["gestation_period"]
                self.newborn_weight = animal["newborn_weight"]
                self.average_weight = animal["average_weight"]
                self.weight_age_ratio = animal["weight/age_ratio"]
                self.food_weight_ratio = animal["food/weight_ratio"]
        if self.gender == "female":
            self.start_pregnancy = 0
        self.chance_of_dying = self.age / self.life_expectancy / 12

    def grow(self, months):
        self.weight += self.weight_age_ratio * months
        self.age += months

    def eat(self):
        for animal in self.species_database["animals"]:
            if self.species == animal["species"]:
                self.weight += self.weight * self.food_weight_ratio / 4
                if self.weight >= self.average_weight:
                    self.weight = self.average_weight

    def die(self):
        chance = random()
        return self.chance_of_dying > chance
