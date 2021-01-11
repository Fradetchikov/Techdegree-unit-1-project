import random



def start_game():

    answer = random.randint(1, 10)
    print("Welcome to the Gessing Game Number! ")
    print(answer)
    attempt_count = 1
    player_try = input("Please enter a number between 1 and 10: ")
    try:
        player_try = int(player_try)
        if player_try < 0 or player_try > 10:
            print("This is not a valid number. Please try again")
        elif player_try < answer:
            print("It is higher!")
        elif player_try > answer:
            print("It is lower")
        elif player_try == answer:
            print("This is the answer we want")
    except ValueError:
        print("This is not a valid value. Try again ...")




start_game()



