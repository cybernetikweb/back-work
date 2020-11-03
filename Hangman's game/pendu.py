# coding: utf-8

from game import game
from function.data import count, list_score
from function.winner import winner
from function.create_data_file import create_data_file

continue_game = True

while continue_game:

    game_launch = input("Entrez Y pour continuer, O pour quitter : ")[0]

    if game_launch.lower() == "y":
        game(count)

    elif game_launch.lower() == "o":
        if len(list_score) > 0:
            winner(list_score)
            create_data_file(list_score)
        continue_game = False

    else:
        print("T'as pas rentré un bon caractères, LIS LA CONSIGNE CONNARD!.")
