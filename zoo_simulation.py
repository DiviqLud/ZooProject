from zoo import Zoo
from animals import Animal
from random import choice
DAYS_IN_WEEK = 7
DAYS_IN_MONTH = 30
DAYS_IN_YEAR = 365


def main():
    print("Hello and welcome to Sofia Zoo!" + "\n"
          "Please, enter one of the following commands:" + "\n"
          "see_animals" + "\n"
          "accommodate <species> <name> <age> <gender> <weight>" + "\n"
          "move_to_habitat <species> <name>" + "\n"
          "simulate <interval_of_time> <period> " + "\n"
          "finish")
    sofia_zoo = Zoo(20, 200)
    intervals_of_time = {1: "days", 2: "weeks", 3: "months", 4: "years"}
    panda = Animal("panda", 32, "Pandio", "male", 50)
    tiger = Animal("tiger", 20, "Tonny", "male", 110)
    tigress = Animal("tiger", 24, "Anne", "female", 75)
    sofia_zoo.accomodate_new_animal(panda)
    sofia_zoo.accomodate_new_animal(tiger)
    sofia_zoo.accomodate_new_animal(tigress)
    command = input("Enter command > ")
    lst = command.split(" ")
    while lst[0] != "finish":
        if lst[0] == "see_animals":
            for animal in sofia_zoo.animals:
                print("{} : {}, {}, {}".format(animal.name,
                      animal.species, animal.age, round(animal.weight, 2)))
        if lst[0] == "accommodate":
            sofia_zoo.accomodate_new_animal(Animal(lst[1],
                                                   lst[3],
                                                   lst[2],
                                                   lst[4],
                                                   lst[5]))
        if lst[0] == "move_to_habitat":
            sofia_zoo.remove_animal(lst[1], lst[2])
        if lst[0] == "simulate":
            print("Simulation of the zoo for {} {}".format(lst[2], lst[1]))
            if lst[1] == intervals_of_time[1]:
                days = lst[2]
            elif lst[1] == intervals_of_time[2]:
                days = lst[2] * DAYS_IN_WEEK
            elif lst[1] == intervals_of_time[3]:
                days = lst[2] * DAYS_IN_MONTH
            else:
                days = lst[2] * DAYS_IN_YEAR
            for animal in sofia_zoo.animals:
                animal.grow(days / DAYS_IN_MONTH)
            print("Animals in the zoo:")
            for animal in sofia_zoo.animals:
                print("{} : {}, {}, {}".format(animal.name,
                                               animal.species,
                                               animal.age,
                                               round(animal.weight, 2)))
                animal.grow(days / DAYS_IN_MONTH)
            for day in range(days):
                for animal in sofia_zoo.animals:
                    animal.eat()
                    if sofia_zoo.die(animal):
                        print(animal.name + " has died")
                sofia_zoo.daily_income()
                sofia_zoo.daily_outcome()
                if sofia_zoo.budget == 0:
                    print("The zoo cannot affor to feed all animals")
                number_of_animals_in_zoo = len(sofia_zoo.animals)
                sofia_zoo.reproduce(choice(sofia_zoo.animals),
                                    choice(sofia_zoo.animals))
                #sofia_zoo.reproduce(tiger, tigress)
                if len(sofia_zoo.animals) > number_of_animals_in_zoo:
                    print("New baby is born")
        command = input("Enter command > ")
        lst = command.split(" ")

if __name__ == '__main__':
    main()
