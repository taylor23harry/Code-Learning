import unittest
from city_functions import format_location

class LocationTestCase(unittest.TestCase):
    """ Tests for 'city_functions.py'. """

    def test_city_location(self):
        """ Does a city and country work? """
        formatted_location = format_location('brussels', 'belgium')
        self.assertEqual(formatted_location, 'Brussels, Belgium')
    
    def test_city_location_pop(self):
        """ Does a city, country and population work? """
        formatted_location = format_location('brussels', 'belgium', '12000000')
        self.assertEqual(formatted_location, 'Brussels, Belgium - Population 12000000')


if __name__ == '__main__':
    unittest.main()