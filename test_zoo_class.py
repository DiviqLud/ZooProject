import unittest
import animals
import zoo


class TestZooClass(unittest.TestCase):
    def setUp(self):
        self.sofia_zoo = zoo.Zoo(2, 2000)
        self.panda = animals.Animal("panda", 5, "Bambi", "female", 40)
        self.frog = animals.Animal("frog", 1, "Kikerica", "female", 10)
        self.cow = animals.Animal("cow", 3, "Moo", "female", 67)

    def test_init(self):
        self.assertEqual(self.sofia_zoo.capacity, 2)
        self.assertEqual(self.sofia_zoo.budget, 2000)

    def test_accommodate_new_animals(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        with self.assertRaises(ValueError):
            self.sofia_zoo.accomodate_new_animal(self.cow)
        self.assertEqual(self.sofia_zoo.animals, [self.panda, self.frog])

    def test_if_there_is_an_animal_with_the_same_name(self):
        self.sofia_zoo.capacity = 50
        frog1 = animals.Animal("frog", 2, "Kikerica", "male", 8)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        with self.assertRaises(ValueError):
            self.sofia_zoo.accomodate_new_animal(frog1)

    def test_daily_income(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        self.assertEqual(self.sofia_zoo.daily_income(), 120)

    def test_daily_outcome(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        grass = 2  # not sure if this is right :D
        self.assertEqual(self.sofia_zoo.daily_outcome(self.panda, grass, 10), 20)

    def test_if_animal_die(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        if self.sofia_zoo.die(self.panda):
            self.assertEqual(self.sofia_zoo.animals, [self.frog])
        else:
            self.assertEqual(self.sofia_zoo.animals, [self.panda, self.frog]).

    def test_newborn(self):
        the_panda = animals.Animal("panda", 5, "Ivo", "male", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_panda)
        #self.sofia_zoo.give_name_to_newborn("Richi")
        self.sofia_zoo.newborn(the_panda, self.panda, "Richie")
        #self.sofia_zoo.reproduce(the_panda, self.panda)
        self.assertEqual(len(self.sofia_zoo.animals), 3)

    #def test_give_name_to_newborn(self):
    #    self.sofia_zoo.newborn()
    #making tests for reproduce function and newborn

if __name__ == '__main__':
    unittest.main()
