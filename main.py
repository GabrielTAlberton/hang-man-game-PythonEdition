import turtle

from game_features import GameCoreFunctions
from screen_config import GameScreen
from writer import Writer

game_screen = GameScreen()
game_functions = GameCoreFunctions()
writer = Writer()

game_screen.game_start_image()

while game_functions.game_is_on:

    if game_functions.tries == 0:
        game_screen.clear()
        game_screen.change_image_loose()
        game_functions.game_win_loose_curio_full_update()
        writer.game_win_lose_write_myst_word(game_functions.mysterious_word_curio)
        game_functions.game_is_on = False
    elif "_" not in game_functions.mysterious_word_display:
        game_screen.clear()
        game_screen.change_image_win()
        game_functions.game_win_loose_curio_full_update()
        writer.game_win_lose_write_myst_word(game_functions.mysterious_word_curio)
        game_functions.game_is_on = False
    else:
        writer.write_myst_word(game_functions.mysterious_word_curio)
        writer.write_wrong_letters(game_functions.wrong_letters)
        game_functions.guess_input()
        if game_functions.guess in game_functions.chosen_word:
            game_functions.right_guess_curio_update()
        else:
            game_functions.wrong_guess_multi_update()

game_screen.screen.mainloop()
