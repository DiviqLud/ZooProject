import unittest
import animals


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal = animals.Animal("tiger", 40, "DiviqLud", "male", 200)

    def test_init(self):
        self.assertEqual(self.animal.species, "tiger")
        self.assertEqual(self.animal.age, 40)
        self.assertEqual(self.animal.name, "DiviqLud")
        self.assertEqual(self.animal.gender, "male")
        self.assertEqual(self.animal.weight, 200)

    def test_if_animal_is_in_life_expectancies(self):
        animal = animals.Animal("panda", 5, "Bambi", "female", 80)
        self.assertEqual(animal.life_expectancy, 100)
        animal2 = animals.Animal("frog", 1, "Kikerica", "female", 10)
        self.assertEqual(animal2.life_expectancy, 50)

    def test_grow(self):
        self.animal.grow(50, 2)
        self.assertEqual(self.animal.weight, 250)
        self.assertEqual(self.animal.age, 42)

    def test_eat_when_overeat(self):
        self.animal.eat(500)
        self.assertEqual(self.animal.weight, 300)

    def test_eat_normal_before_overweight(self):
        self.animal.eat(100)
        self.assertEqual(self.animal.weight, 225)

    def test_if_the_animal_can_die(self):
        results = []
        for i in range(100):
            results.append(self.animal.die())
        print(results)
        self.assertTrue(True in results and False in results)

if __name__ == '__main__':
    unittest.main()
