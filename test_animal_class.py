import unittest
import animals


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = animals.Animal("tiger", 36, "DiviqLud", "male", 200)

    def test_init(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 36)
        self.assertEqual(self.animal.name, "DiviqLud")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 200)

    def test_if_animal_is_in_life_expectancies(self):
        animal = animals.Animal("panda", 5, "Bambi", "female", 80)
        self.assertEqual(animal.life_expectancy, 25)
        animal2 = animals.Animal("tiger", 10, "Bo", "male", 100)
        self.assertEqual(animal2.life_expectancy, 15)

    def test_grow(self):
        self.animal.grow(3)
        self.assertEqual(self.animal.weight, 209)
        self.assertEqual(self.animal.age, 39)

    def test_eat_normal(self):
        self.animal.eat()
        self.assertEqual(self.animal.weight, 203.5)

    def test_eat_overweight(self):
        self.animal.grow(200)
        self.animal.eat()
        self.assertEqual(self.animal.weight, 300)

    def test_if_the_animal_can_die(self):
        results = []
        for i in range(100):
            results.append(self.animal.die())
        self.assertTrue(True in results and False in results)

if __name__ == '__main__':
    unittest.main()
