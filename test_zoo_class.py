import unittest
import animals
import zoo


class TestZooClass(unittest.TestCase):
    def setUp(self):
        self.sofia_zoo = zoo.Zoo(2, 200000)
        self.panda = animals.Animal("panda", 5, "Bambi", "female", 80)
        self.frog = animals.Animal("frog", 1, "Kikerica", "female", 10)
        self.cow = animals.Animal("cow", 3, "Moo", "female", 67)

    def test_init(self):
        self.assertEqual(self.sofia_zoo.capacity, 2)
        self.assertEqual(self.sofia_zoo.budget, 200000)

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
        self.assertEqual(self.sofia_zoo.daily_income(), 6)

    def test_daily_outcome(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        self.assertEqual(self.sofia_zoo.daily_outcome(), 4)

    def test_if_animal_die(self):
        self.sofia_zoo.accomodate_new_animal(self.panda)
        self.sofia_zoo.accomodate_new_animal(self.frog)
        self.panda.die()
        self.assertEqual(self.sofia_zoo.animals, [self.frog])

    def test_give_name_to_newborn(self):
        self.sofia_zoo.newborn()
