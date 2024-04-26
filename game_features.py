# imports #
from game_words import word_list
import random
from screen_config import GameScreen
from turtle import Turtle
import turtle

# constants #
MYST_WORD_FONT = ("Courier", 24, "normal")
WRONG_LETTERS_FONT = ("Courier", 12, "normal")


# class definition #
class GameCoreFunctions(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.chosen_word = random.choice(word_list)
        self.mysterious_word_display = ["_" for letter in self.chosen_word]
        self.mysterious_word_curio = f"{' '.join(self.mysterious_word_display)}"
        self.tries = 6
        self.guess = ""
        self.wrong_letters = []
        self.screen_counter = 1

    # input window to player guess a letter #
    def guess_input(self):
        letters_left = sum(element.lower().count("_") for element in self.mysterious_word_display)
        guess_scr = turtle.Screen()
        self.guess = guess_scr.textinput(
            title=f"{letters_left} letters left to guess",
            prompt="Guess a letter:"
        ).lower()

    def curio_update(self):
        self.mysterious_word_curio = f"{' '.join(self.mysterious_word_display)}"

    def right_guess_curio_update(self):
        for index_pos, letter in enumerate(self.mysterious_word_display):
            if self.guess == letter:
                self.mysterious_word_display[index_pos] = letter
                self.curio_update()


# wrd = random.choice(word_list)
# print(wrd)
# wrd_display = ["_" for letter in wrd]
# print(wrd_display)
# wrd_curio = f"{' '.join(wrd_display)}"
# print(wrd_curio)
# wrd_display[2] = "G"
# wrd_curio = f"{' '.join(wrd_display)}"
# print(wrd_curio)