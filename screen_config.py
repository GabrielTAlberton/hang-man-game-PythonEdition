# imports #
import turtle
from turtle import Turtle


# class definition #
class GameScreen(Turtle):

    # super class to use screen configuration from the turtle library #
    def __init__(self):
        super().__init__()
        self.hideturtle()
        game_screen = turtle.Screen()
        game_screen.title("The Hangman Game")
        game_screen.setup(1200, 650)
        self.background_image = "hang-man-game-rules.gif"
        turtle.addshape(self.background_image)
        turtle.shape(self.background_image)

    # change to the first instance of gameplay image #
    def game_start_image(self):
        self.background_image = "hang-man-game-0.gif"

    # change the image when the player take a wrong guess #
    def change_image_wrong_guess(self, x):
        self.background_image = f"hang-man-game-{x}.gif"
        turtle.addshape(self.background_image)
        turtle.shape(self.background_image)

    # change image if player looses the game #
    def change_image_loose(self):
        self.background_image = "hang-man-game-loose.gif"
        turtle.addshape(self.background_image)
        turtle.shape(self.background_image)

    # change image if player wins the game #
    def change_image_win(self):
        self.background_image = "hang-man-game-win.gif"
        turtle.addshape(self.background_image)
        turtle.shape(self.background_image)
