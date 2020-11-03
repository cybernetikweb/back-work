def get_username():
    print(
        "Tu as commencer une nouvelle partie \nTu commence avec un score de zero. Le nombre d'occasion restante correspondra à ton score")
    user_name = input("Entre un nom sale shlag : ")
    while len(user_name) == 0:
        print("Ta rentrée aucun nom respect la consigne connar!")
        user_name = input("Entre un nom sale shlag : ")
    return user_name
