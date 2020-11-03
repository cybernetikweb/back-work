from function.data import list_score, filter_word
from function.letter_not_found import letter_not_found
from function.letter_found import letter_found
from function.word_not_found import user_lost
from function.word_found import user_won
import random


def game(count):
    print(
        "Tu as commencer une nouvelle partie \nTu commence avec un score de zero. Le nombre d'occasion restante correspondra à ton score")
    user_name = input("Entre un nom sale shlag : ")
    while len(user_name) == 0:
        print("Ta rentrée aucun nom respect la consigne connar!")
        user_name = input("Entre un nom sale shlag : ")

    word = random.choice(filter_word)
    chance_number = len(word) + 6
    word_found = []
    for _ in word:
        word_found.append("*")

    while word_found != word:
        count += 1
        if count > chance_number:
            user_lost(word)
            break

        if count == 1:
            print(word_found)
        user_letter = input("Veuillez choisir une lettre : ")[0].lower()
        if not user_letter.isalpha():
            print("Vous avez entré un chiffre ou un caractère spécial, les mots ne contiennent que des lettres")
            user_letter = input("Veuillez choisir une lettre : ")[0].lower()

        if user_letter in word:
            letter_found(word_found, word, user_letter)

            if chance_number > 0 and ''.join(map(str, word_found)) == word:
                user_won(word_found, chance_number, count, user_name, list_score)
                break

        else:
            letter_not_found(word_found, chance_number, count)
    return word
