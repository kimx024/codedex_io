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

class CoffeeMenu:
    def __init__(self):
        self.menu = {
            'espresso': 2.50,
            'latte': 2.75,
            'cappuccino': 3.20,
            'americano': 2.70
        }

    # A function that returns the price of an item of the menu in lowercase
    def get_price(self, item):
        return self.menu.get(item.lower())

    # A function that adds a new item to the list
    def add_item(self, item, price):
        self.menu[item.lower()] = price


menu = CoffeeMenu()
