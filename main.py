# Author Name: Talluri Lakshman Sai, Naramreddy Manoj Sai, Haveela E Joycy Ramakuri
# Date: 12/07/2023
# Description: The main file that runs the game

from GameEngine import GameEngine


def main():
    # Instantiate the GameEngine object
    game_engine = GameEngine()

    # Initialize the game
    game_engine.initialize_game()

    # Display the game's introduction
    game_engine.intro()

    # Initialize the number of remaining vegetables
    remaining_veggies = game_engine.remaining_veggies()

    # Main game loop
    while remaining_veggies > 0:
        print(f"{remaining_veggies} veggies remaining. Current score: {game_engine.get_score()}")
        game_engine.print_field()
        game_engine.move_rabbits()
        game_engine.move_captain()
        game_engine.move_snake()

        remaining_veggies = game_engine.remaining_veggies()

    # Game over
    game_engine.game_over()

if __name__ == "__main__":
    main()