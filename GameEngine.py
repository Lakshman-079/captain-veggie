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
                # get the dimensions(rows, columns)
                lines = file.readlines()
                dimensions = lines[0].strip().split(",")[1:]
                rows, cols = int(dimensions[0]), int(dimensions[1])
                self._field = [[None for _ in range(cols)] for _ in range(rows)]

                for line in lines[1:]:
                    name, symbol, points = line.strip().split(',')
                    self._possible_veggies.append(Veggie(name, symbol, int(points)))

                # set the veggies in random places in the field
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

    def remaining_veggies(self):
        """
        Counts and returns the number of remaining vegetables on the field.
        """
        return sum(1 for row in self._field for item in row if isinstance(item, Veggie))
    
    def intro(self):
        """
        Prints the introductory message for the game, explaining the premise and goal.
        Also lists the vegetables available in the game along with their point values.
        """
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest as many vegetables as possible before the rabbits eat them all! Each vegetable is worth a different number of points so go for the high score!\\n")

        print("The vegetables are:")

        [print(f"{veggie.get_symbol()}: {veggie.get_name()} {veggie.get_points()} points") for veggie in self._possible_veggies]
        
        print("\\nCaptain Veggie is V, and the rabbits are R's.\\n")
        print("Good luck!")

    def print_field(self):
        """
        Prints the current state of the game field in a formatted 2D grid.
        """
        rows = len(self._field)
        cols = len(self._field[0]) if rows > 0 else 0

        # Create the top and bottom borders based on the number of columns
        border = '#' * (cols * 3 + 2)  # 2 spaces per symbol + 3 for borders and space

        print(border)
        for row in self._field:
            print("#", end="")
            for item in row:
                symbol = item.get_symbol() if item is not None else " "
                print(symbol.center(3), end="")  # spaces for padding
            print("#")
        print(border)


    def get_score(self):
        """
        Returns the current score of the player.
        """
        return self._score

    def move_rabbits(self):
        """
        Moves each rabbit on the field. Rabbits can move in any direction or stay put.
        If a rabbit moves to a spot with a vegetable, the vegetable is removed.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)] # 8 directions + stay
        rows, cols = len(self._field), len(self._field[0])

        for rabbit in self._rabbits:
            dx, dy = random.choice(directions)
            new_x, new_y = rabbit.get_x() + dx, rabbit.get_y() + dy

            if 0 <= new_x < rows and 0 <= new_y < cols: # this is for covering corner case for not trying to move outside the field borders
                if self._field[new_x][new_y] is None or isinstance(self._field[new_x][new_y], Veggie):
                    if isinstance(self._field[new_x][new_y], Veggie):
                        self._field[new_x][new_y] = None
                    self._field[rabbit.get_x()][rabbit.get_y()] = None
                    rabbit.set_x(new_x)
                    rabbit.set_y(new_y)
                    self._field[new_x][new_y] = rabbit
            else:
                new_x, new_y = rabbit.get_x(), rabbit.get_y()

    def move_cpt_vertical(self, movement):
        """
        Prompts the player for a movement direction and moves the captain accordingly.
        """
        new_x = self._captain.get_x() + movement
        if 0 <= new_x < len(self._field):
            self._move_captain(new_x, self._captain.get_y())


    def move_cpt_horizontal(self, movement):
        """
        Moves the captain horizontally based on the specified movement value.

        Args:
            movement (int): The amount to move horizontally. Negative for left, positive for right.
        """
        new_y = self._captain.get_y() + movement
        if 0 <= new_y < len(self._field[0]):
            self._move_captain(self._captain.get_x(), new_y)

    def _move_captain(self, new_x, new_y):
        """
        Moves the captain to a new location on the field.

        Args:
            new_x (int): The new x-coordinate for the captain.
            new_y (int): The new y-coordinate for the captain.
        """
        current_x, current_y = self._captain.get_x(), self._captain.get_y()
        target = self._field[new_x][new_y]

        if target is None or isinstance(target, Veggie):
            self._field[current_x][current_y] = None
            self._captain.set_x(new_x)
            self._captain.set_y(new_y)
            self._field[new_x][new_y] = self._captain

            if isinstance(target, Veggie):
                print(f"Yummy! A delicious {target.get_name()}")
                self._captain.add_veggie(target)
                self._score += target.get_points()

        elif isinstance(target, Rabbit):
            print("Don't step on the bunnies!")

    def move_captain(self):
        """
        Prompts the player for a direction and moves the captain accordingly.
        Accepts input for up, down, left, or right movement.
        """
        direction = input("Would you like to move up(W), down(S), left(A), or right(D): ").lower()
        if direction == 'w':
            self.move_cpt_vertical(-1)
        elif direction == 's':
            self.move_cpt_vertical(1)
        elif direction == 'a':
            self.move_cpt_horizontal(-1)
        elif direction == 'd':
            self.move_cpt_horizontal(1)
        else:
            print(f"{direction} is not a valid option")


    def game_over(self):
        """
        Handles the end of the game.
        Outputs the harvested vegetables and the final score.
        """
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veggie in self._captain.get_veggies_collected():
            print(veggie.get_name())
        print(f"Your score was: {self._score}")
        self.high_score()

    def high_score(self):
        """
        Manages the high score functionality.
        Loads existing high scores, updates them with the current game's score, and saves back.
        """
        high_scores = []
        if os.path.exists(GameEngine.HIGHSCOREFILE):
            with open(GameEngine.HIGHSCOREFILE, 'rb') as file:
                high_scores = pickle.load(file)

        initials = input("Please enter your three initials: ")[:3]
        new_score = (initials, self._score)
        high_scores.append(new_score)
        high_scores.sort(key=lambda x: x[1], reverse=True)

        print("HIGH SCORES")
        print("Name\tScore")
        for score in high_scores:
            print(f"{score[0]}\t\t{score[1]}")

        with open(GameEngine.HIGHSCOREFILE, 'wb') as file:
            pickle.dump(high_scores, file)

