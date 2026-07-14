#Number Guessing Game
Secret_num = 56
guess = int(input("Guesss the correct number to win the game: "))
while True:
    if guess == Secret_num:
        print("You have won the game")
        break
    else:
        print("incorrect guess, Please try again")
        guess = int(input("Guess the number again to win the game: "))
        continue

    