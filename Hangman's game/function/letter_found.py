def letter_found(word_found, word, user_letter):
    list_of_indices = [i for i, x in enumerate(word) if x == user_letter]

    if len(list_of_indices) == 1:
        word_found[word.index(user_letter)] = user_letter
    else:
        for el in list_of_indices:
            word_found[el] = user_letter

    if "*" in word_found:
        print(word_found)
