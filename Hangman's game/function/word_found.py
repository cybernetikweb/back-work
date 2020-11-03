import random


def user_won(word_found, chance_number, count, user_name, list_score):
    word_for_looser = ["cash a drare", "monney mgl", "asperger", "pepet"]
    word_found = ''.join(map(str, word_found))
    point = chance_number - count
    print("Wesh, ce n'était qu'une question de %s, le mot était : %s, nombre de point gagner %d" % (
        random.choice(word_for_looser), word_found, point))

    array_of_keys = list(list_score)

    if len(list_score) == 0:
        list_score[user_name] = point

    else:
        if user_name in array_of_keys:
            list_score[user_name] += point
        else:
            list_score[user_name] = point
    print(list_score)
