n = 18
print("No of guesses are limited to 9 only")
no_of_guesses = 1

while no_of_guesses<=9:
    print("Enter your Guess :", end=" ")
    guess = int(input())
    
    if guess<18:
        print("Enter a higher number please.",9-no_of_guesses,"no. of guesses are left")
    elif guess>18:
        print("Enter a lower number please.",9-no_of_guesses,"no. of guesses are left")
    else:
        print("Congratulations! You won.","You took",no_of_guesses,"guesses to finish the game")
        break

    no_of_guesses = no_of_guesses + 1

    if no_of_guesses>9:
        print("Game over! You exhausted all of your guesses")
        break
    

