import unittest
import animals
import zoo


class TestZooClass(unittest.TestCase):
    def setUp(self):
        self.sofia_zoo = zoo.Zoo(20, 2000)
        self.panda = animals.Animal("panda", 24, "Bambi", "female", 40)
        self.tiger = animals.Animal("tiger", 36, "Tigercho", "male", 10)
        self.lion = animals.Animal("lion", 48, "Mufasa", "male", 67)

    def test_init(self):
        self.assertEqual(self.sofia_zoo.capacity, 20)
        self.assertEqual(self.sofia_zoo.budget, 2000)

    def test_accommodate_new_animals(self):
        self.sofia_zoo.capacity = 2
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.tiger)
        with self.assertRaises(ValueError):
            self.sofia_zoo.accomodate_new_animal(self.lion)
        self.assertEqual(self.sofia_zoo.animals, [self.panda, self.tiger])

    def test_if_there_is_an_animal_with_the_same_name(self):
        frog1 = animals.Animal("tiger", 2, "Tigercho", "male", 8)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.tiger)
        with self.assertRaises(ValueError):
            self.sofia_zoo.accomodate_new_animal(frog1)

    def test_daily_income(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.tiger)
        self.assertEqual(self.sofia_zoo.daily_income(), 120)

    def test_daily_outcome(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.tiger)
        self.assertEqual(self.sofia_zoo.daily_outcome(), 4.81)

    def test_if_animal_die(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.tiger)
        if self.sofia_zoo.die(self.panda):
            self.assertEqual(self.sofia_zoo.animals, [self.tiger])
        else:
            self.assertEqual(self.sofia_zoo.animals, [self.panda, self.tiger])

    def test_newborn(self):
        the_panda = animals.Animal("panda", 5, "Ivo", "male", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_panda)
        self.sofia_zoo.newborn(the_panda, self.panda)
        self.assertEqual(len(self.sofia_zoo.animals), 3)

    def test_give_name_to_newborn(self):
        the_panda = animals.Animal("panda", 5, "Ivo", "male", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_panda)
        self.sofia_zoo.newborn(the_panda, self.panda)

    def test_reproduce_if_two_female(self):
        the_panda = animals.Animal("panda", 5, "Ivo", "female", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_panda)
        self.sofia_zoo.reproduce(the_panda, self.panda)
        self.assertEqual(len(self.sofia_zoo.animals), 2)

    def test_normal_reproduce(self):
        the_panda = animals.Animal("panda", 5, "Ivo", "male", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_panda)
        self.sofia_zoo.reproduce(the_panda, self.panda)
        self.assertEqual(len(self.sofia_zoo.animals), 3)

    def test_reproduce_with_different_species(self):
        the_tiger = animals.Animal("tiger", 5, "Ivo", "male", 55)
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(the_tiger)
        self.sofia_zoo.reproduce(the_tiger, self.panda)
        self.assertEqual(len(self.sofia_zoo.animals), 2)


if __name__ == '__main__':
    unittest.main()
