import random

while True:
    secret_number = random.randrange(1, 10, 1)

    limit = 3
    tries = 0
    has_guessed_correctly = False
    while not has_guessed_correctly:
        user_guess = int(input("Guess a number: "))
        print(f"You have guessed {user_guess}")
        limit = limit - 1
        tries = tries + 1
        print(f"You have {limit} more tries left")

        difference = secret_number - user_guess
        difference = abs(difference)
        print(f"This is your {tries} attempt")

        if difference == 0:
            print("You have guessed correctly!")
            has_guessed_correctly = True
            exit()

        else:
            if limit == 0:
                print("Game over")

                print("Do you want to try again?")
                to_continue = input("yes/no ")
                if to_continue.strip() == "yes":
                    to_continue = True
                else:
                    to_continue = False
                if not to_continue:
                    exit()
                else:
                    has_guessed_correctly = True

            if difference <= 2:
                print("You are very close!")
            elif difference <= 5:
                print("Ypu are halfway there!")
            else:
                print("You are more than halfway there!")
            print("You have guessed incorrectly, try again!")
        print("\n")
