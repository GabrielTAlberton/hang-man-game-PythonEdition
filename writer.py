from turtle import Turtle
from game_features import GameCoreFunctions

FONT_MYST_WORD = ("Courier", 48, "normal")
FONT_MYST_REVEALED = ("Courier", 35, "normal")
FONT_WRONG_LETTERS = ("Courier", 12, "normal")


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.game_functions = GameCoreFunctions()

    def walk_to(self, x, y):
        self.goto(x, y)

    def write_myst_word(self, word_curio):
        self.goto(-230, -170)
        self.clear()
        self.write(word_curio, align="left", font=FONT_MYST_WORD)

    def write_wrong_letters(self, wrong_letters_list):
        self.goto(325, 120)
        self.write(wrong_letters_list, font=FONT_WRONG_LETTERS)

    def game_win_lose_write_myst_word(self, word_curio):
        self.goto(-110, -179)
        self.clear()
        self.write(word_curio, font=FONT_MYST_REVEALED)
