import random


def winner(list_score):
    word_for_looser = ["baptou", "bandeur", "hmar", "asperger", "arouf",
                       "qlp", "maahdel", "kurwa", "noichi",
                       "soviet"]

    all_values = list(list_score.values())
    max_values = max(all_values)
    winner_name = [key for (key, value) in list_score.items() if value == max_values][0]
    print("%s à gagné, avec un score de %s, les autres ce sont tous des %s" % (
        winner_name, max_values, random.choice(word_for_looser)))
