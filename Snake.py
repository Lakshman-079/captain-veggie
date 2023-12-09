# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Class for Snake that is a subclass of Creature

from Creature import Creature

class Snake(Creature):
    def __init__(self, x, y):
        """
        Initialize a Snake object at given coordinates with the symbol 'S'.

        Args:
            x (int): The x-coordinate of the snake on the field.
            y (int): The y-coordinate of the snake on the field.
        """
        super().__init__(x, y, "S")
