# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Class for Veggie that is a subclass of FieldInhabitant that sets and gets the name and points for the veggies

from FieldInhabitant import FieldInhabitant


class Veggie(FieldInhabitant):
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points

    def __str__(self):
        return f"{self._symbol} - {self._name}: {self._points} Points"

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points

