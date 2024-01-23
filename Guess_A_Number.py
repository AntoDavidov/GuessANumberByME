import random
while True:
    number = (random.randrange(0, 101))
    guess = 0
    best_score = float('inf')
    while True:
        number_guess = int(input("Take a guess:"))
        try:
            number_guess = int(number_guess)
            if number_guess not in range(0, 101):
                print("Please enter a number between 1-100")
                continue

            guess += 1
            if number_guess == number:
                print(f"You guessed it. It took you {guess} attempts")
                if guess < best_score:
                    best_score = guess
                    print(f"New best record: {best_score} attempts!")
                else:
                    print(f"Best record: {best_score} attempts.")
                break

            elif number_guess < number:
                print("Hint: Too low!")
            else:
                print("Hint: Too high")
        except ValueError:
            print("Enter a valid number")
    play_again = input("Do you want to play again? (yes/no):").lower()
    if play_again != "yes":
        break