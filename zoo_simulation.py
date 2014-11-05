from zoo import Zoo
from animals import Animal


def main():
    print("Hello and welcome to Sofia Zoo!" + "\n"
          "Please, enter one of the following commands:" + "\n"
          "see_animals" + "\n"
          "accommodate <species> <name> <age> <gender> <weight>" + "\n"
          "move_to_habitat <species> <name>" + "\n"
          "simulate <interval_of_time> <period>" + "\n"
          "finish")
    sofia_zoo = Zoo(20, 2000)
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
                print("{} : {}, {}, {}".format(animal.name, animal.species, animal.age, animal.weight))
        if lst[0] == "accommodate":
            sofia_zoo.accomodate_new_animal(Animal(lst[1], lst[3], lst[2], lst[4], lst[5]))
        if lst[0] == "move_to_habitat":
            sofia_zoo.remove_animal(lst[1], lst[2])
        command = input("Enter command > ")
        lst = command.split(" ")

if __name__ == '__main__':
    main()
