from random_word import RandomWords
"""import a class to find a random word"""

r = RandomWords()
#current_word = r.get_random_word()
current_word_letters = []
hanged_letters = []
turns = 7
active = True
tick = 1

while active:
    current_word=r.get_random_word()
    length_of_word=len(current_word)

    for letters in current_word:
        current_word_letters.append(letters.lower())
        hanged_letters.append("")

    print("You have seven turns to guess the right answer: ")
    print("The word you are trying to guess is " + str(length_of_word) + " letters long.")


    while turns > 0:
        current_guess=input("What letter would you like to guess? ")
        if current_guess.lower() in current_word_letters:
            for part in current_word_letters:
                tickspot = tick - 1
                if part.lower() == current_guess.lower():
                    print("Your letter appears in spot " + str(tick))
                    #print(tickspot)
                    if hanged_letters[tickspot] == "":
                        hanged_letters[tickspot] = str(current_guess.lower())
                        #print(hanged_letters)
                else:
                    #print(tickspot)
                    if hanged_letters[tickspot] == "":
                        hanged_letters[tickspot] = ""

                tick += 1


        else:
            print("Sorry, that letter is not in the word you're guessing")

        print(hanged_letters)

        if turns > 1:
            guess = input("Would you like to guess the answer? Please answer yes or no? ")
            if guess == "yes":
                guess = input("What is your guess? ")
                if guess.lower() == current_word.lower():
                    print("Congratulations, you've won!")
                    break
                else:
                    print("Sorry, you dope. You've lost")
                    print("The correct word was " + current_word + ".")
                    break

        if turns == 1:
            print("You must guess as this is your final turn: ")
            guess = input("What is your guess?")
            if guess.lower() == current_word.lower():
                print("Congratulations, you've won!")
                break
            else:
                print("Sorry, you dope. You've lost")
                print("The correct word was " + current_word + ".")
                break

        turns -= 1
        print("You have " + str(turns) + " turns remaining.")
        tick = 1



    play_again=input('Do you want to play again? Please answer "yes" or "no"')
    if play_again == "no":
        active = False
    tick = 1
    hanged_letters = []
    current_word_letters = []
    turns = 7
