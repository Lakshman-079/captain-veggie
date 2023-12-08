# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: Main Game Engine logic that can control the movement of rabbit, captain , snake and veggies.

import os
import pickle
import random

from Captain import Captain
from Creature import Creature
from FieldInhabitant import FieldInhabitant
from Rabbit import Rabbit
from Veggie import Veggie


class GameEngine:
    NUMBEROFVEGGIES = 30
    NUMBEROFRABBITS = 5
    HIGHSCOREFILE = "highscore.data"

    def __init__(self):
        """
        Initialize the GameEngine with default settings.
        This sets up empty lists for the field, rabbits, and possible veggies,
        along with the captain object and score.
        """
        self._field = []
        self._rabbits = []
        self._captain = None
        self._possible_veggies = []
        self._score = 0

    def init_veggies(self):
        """
        Initializes vegetables in the game field.
        Reads veggie data from a user-provided file and populates the field with veggies.
        """
        filename = input("Enter the name of the veggie file: ")
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                dimensions = lines[0].strip().split(",")[1:]
                rows, cols = int(dimensions[0]), int(dimensions[1])
                self._field = [[None for _ in range(cols)] for _ in range(rows)]

                for line in lines[1:]:
                    name, symbol, points = line.strip().split(',')
                    self._possible_veggies.append(Veggie(name, symbol, int(points)))

                for _ in range(GameEngine.NUMBEROFVEGGIES):
                    veggie = random.choice(self._possible_veggies)
                    x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
                    while self._field[x][y] is not None:
                        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
                    self._field[x][y] = veggie
        except FileNotFoundError:
            print("File not found. Please try again.")
            self.init_veggies()

    def init_captain(self):
        """
        Initializes the captain in the game field.
        Places the captain at a random location on the field.
        """
        rows, cols = len(self._field), len(self._field[0])
        x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while self._field[x][y] is not None:
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
        self._captain = Captain(x, y)
        self._field[x][y] = self._captain

    def init_rabbits(self):
        """
        Initializes rabbits in the game field.
        Places a specified number of rabbits at random locations on the field.
        """
        rows, cols = len(self._field), len(self._field[0])
        for _ in range(GameEngine.NUMBEROFRABBITS):
            x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            while self._field[x][y] is not None:
                x, y = random.randint(0, rows - 1), random.randint(0, cols - 1)
            rabbit = Rabbit(x, y)
            self._rabbits.append(rabbit)
            self._field[x][y] = rabbit

    def initialize_game(self):
        """
        Initializes the game by setting up veggies, captain, and rabbits on the field.
        This is the main method to start the game setup.
        """
        self.init_veggies()
        self.init_captain()
        self.init_rabbits()

