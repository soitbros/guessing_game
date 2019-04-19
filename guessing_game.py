import random

def guessing_game():
    while True:
        level = input("Easy/Hard? ")
        if (not level.lower() == 'hard') and (not level.lower() == 'easy'):
            print("That's not an option.")
            continue
        else:
            break
    guesses = 0
    x = random.randint(1,100)
    y = input("I'm thinking of a number between 1 and 100. Can you guess it? ")
    end_game = False
    while end_game == False:
        if (level.lower() == 'hard') & (guesses == 2):
            end_game = True
            again = input("Too many guesses. Game over. Play again? Yes/no? ")
            if again.lower() == 'yes':
                guessing_game()
        elif y.isdigit() == False:
            y = input("I only recognize whole numbers from 1 to 100. Can you guess which one I'm thinking of? ")
        elif 101 > int(y) > x:
            guesses += 1
            y = input("That's too high. Guess again! ")
        elif 0 < int(y) < x :
            guesses += 1
            y = input("That's too low. Guess again! ")
        elif int(y) == x:
            guesses += 1
            end_game = True
            again = input("You got it! You won after guessing " + str(guesses) + " times! Play again? Yes/no? ")
            if again.lower() == 'yes':
                guessing_game()
        else:
            y = input("That's not between 1 and 100. Quit playing around! Guess again. ")

guessing_game()
