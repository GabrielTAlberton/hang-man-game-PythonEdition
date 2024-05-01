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
        self.screen_func = GameScreen()
        self.game_is_on = True

    # input window to player guess a letter #
    def guess_input(self):
        letters_left = sum(element.lower().count("_") for element in self.mysterious_word_display)
        guess_scr = turtle.Screen()
        self.guess = guess_scr.textinput(
            title=f"{letters_left} letters left to guess",
            prompt="Guess a letter:"
        ).lower()

    # game mysterious word display UI update #
    def curio_update(self):
        self.mysterious_word_curio = f"{' '.join(self.mysterious_word_display)}"

    # replace the _ placeholder to the right letter guessed #
    def right_guess_curio_update(self):
        for index_pos, letter in enumerate(self.chosen_word):
            if self.guess == letter:
                self.mysterious_word_display[index_pos] = letter
                self.curio_update()

    # update thresholds if player guesses wrong #
    def wrong_guess_multi_update(self):
        if self.guess not in self.wrong_letters:
            self.wrong_letters.append(self.guess)
            self.screen_func.change_image_wrong_guess(self.screen_counter)
            if self.screen_counter < 5:
                self.screen_counter += 1
                self.tries -= 1
            elif self.screen_counter == 5:
                self.tries -= 1

    def game_win_loose_curio_full_update(self):
        self.mysterious_word_display = []
        self.mysterious_word_display = [letter for letter in self.chosen_word]
        self.curio_update()
