# Authors: Kai Francis, Ryan Yonek
# Date: 8/28/24
# Unit Testing for Inheritance Class Method

# Unit tests
import unittest

# Base class
class Sport:
    def __init__(self, name):
        self.name = name

    def get_equipment(self):
        return "Generic sports equipment"
    
# Derived class
class Basketball(Sport):
    def __init__(self, name, team_size):
        super().__init__(name)
        self.team_size = team_size

    def get_equipment(self):
        return "Basketball"



class TestBasketball(unittest.TestCase):

    def test_get_equipment(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.get_equipment(), "Basketball")

    def test_team_size(self):
        game = Basketball("Basketball", 5)
        self.assertEqual(game.team_size, 5)
    
if __name__ == "__main__":
    unittest.main()



        