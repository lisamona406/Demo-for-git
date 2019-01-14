# building guessing game with while loop

#method 1
#secret_word = "giraffe"
#guess = ""

#while guess != secret_word:
    #guess = input("Enter guess  :")

#print("You win")

secret_word = "giraffe"
guess = ""
guess_count =0
guess_limit=3
out_of_guesses = False # it is boolean whether or not the user is out of guess

while guess != secret_word and not(out_of_guesses) :
    if guess_count < guess_limit :
        guess = input("Enter guess :")
        guess_count+=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You win!")