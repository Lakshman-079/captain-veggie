# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Class for Captain which is a subclass of Creature that gets the veggies collected by the captain

from Creature import Creature


class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._veggies_collected = []

    def add_veggie(self, veggie):
        self._veggies_collected.append(veggie)

    def get_veggies_collected(self):
        return self._veggies_collected

