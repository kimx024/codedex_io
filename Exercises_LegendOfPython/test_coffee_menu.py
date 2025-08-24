"""
The Legend of Python: Intermediate
This code is part of Exercise 20: Caffeinated
This exercise wraps up the last exercise of the Chapter and is the last exercise of the Intermediate Python course

This chapter was about Testing in Python
In this chapter, we learned about:
- What unit testing is and why we use it.
- Writing tests in Python with the unittest framework.
- Defining test cases with the unittest.TestCase class.
- Using assertion methods like .assertEqual() to check expected outcomes.
- Testing object-oriented code, including with setUp() and tearDown() methods.
"""

import unittest
from coffee_menu import CoffeeMenu

class CoffeeMenuTest(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()

    def tearDown(self):
        self.menu =None

    # Test if a latte, which is on the menu, costs value 3
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)


    # Test if a coffee, which is not on the menu, costs value 2
    def test_get_price_non_existing_item(self):
        self.assertEqual(self.menu.get_price('macha'), None)

    # Test if we can add an item to the menu
    def test_add_item(self):
        self.menu.add_item('macha', 4.00)


if __name__ == '__main__':
    unittest.main()



