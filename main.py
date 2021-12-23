import random
name = input("What is your name? ")


def play_game():
    num = random.randint(1, 10)
    print(name + ", Guess a number between 1 and 10: ")
    num_guess = 0
    while num_guess < 5:
        guess = int(input())
        num_guess += 1
        if guess < num:
            print("Your guess is too low")
        if guess > num:
            print("Your guess is too high")
        if guess == num:
            break

    if guess == num:
        print("You guessed the number correctly in " + str(num_guess) + " tries!")
    else:
        print("You guessed the number incorrectly. The number was " + str(num))

    userInput = input("Would you like to play again? ")

    if userInput == "yes" or userInput == "y":
        play_game()
    elif userInput == "no" or userInput == "n":
        print("Thanks for playing!")
    else:
        print("Error")


play_game()
