# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Class for Rabbit that is a subclass of Creature

from Creature import Creature


class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")
