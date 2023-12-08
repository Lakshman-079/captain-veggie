# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Class for FieldInhabitant which is a superclass of Creature and Captain that sets the symbol for the creatures and captain

class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol
