import random
import time


print('Welcome to Hangman!')
time.sleep(2)
name = input('What is your name? ')
print('Hello ' + name + '.  The game will start shortly.')
time.sleep(3)


def main():
    global count
    count = 0
    global already_guessed
    already_guessed = []
    global limit
    limit = 5
    global words
    words = ["dog", "mandible", "gorgeous", "canticle", "sparrow", "superb", "apple", "quarter"]
    while(1):
        play_game()


def hangman_display(count):
    if count == 1:
        print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |            | \n"
            "  |             \n"
            "  |             \n"
        "    ----- " )
        print('Just the head and the torso.  But be careful!')
    elif count == 2:
        print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |            |\ \n"
            "  |             \n"
            "  |             \n"
        "    ----- " )
        print('An arm has been added to the mix.  Remember what I said about being careful.')
    elif count == 3:
        print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |           /|\ \n"
            "  |             \n"
            "  |             \n"
        "    ----- " )
        print('Almost a full human!  You better shape up, friend!')
    elif count == 4:
        print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |           /|\ \n"
            "  |             \ \n"
            "  |             \n"
        "    ----- " )
        print('One more slip up and you\'ll meet your end!')
    elif count == 5:
        print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |           /|\ \n"
            "  |           / \ \n"
            "  |             \n"
        "    ----- " )
        print('I\'m sorry, but you are dead.  Better luck next time!')
        already_guessed.clear()
    else:
        return

def play_game():
    print("-------------\n"
             " |            |\n"
             " |            |\n"
            "  |            O\n"
            "  |             \n"
            "  |             \n"
            "  |             \n"
        "    ----- " )
    word = random.choice(words)
    display = ""
    for x in range(len(word)):
        display += '_'
    count = 0
    while count != 5:
        number_of_letters = 0
        already_guessed_string = ', '.join(already_guessed)
        print('You have already guessed these letters: ' + already_guessed_string)
        guess = input("Here is the word: " + display + " Guess a letter: ")
        if guess.isalpha() and len(guess) == 1:
            lower_guess = guess.casefold()
            if already_guessed.count(lower_guess) > 0:
                print('You already guessed that letter.  Try again!')
                continue
            for y in range(len(word)):
                if word[y] == lower_guess:
                    number_of_letters += 1
                    display_list = [char for char in display]
                    display_list[y] = lower_guess
                    display = ''.join(display_list)
            if number_of_letters == 1:
                print('There was 1 ' + lower_guess + ' in the word.')
            elif number_of_letters > 1:
                print('There were ' + str(number_of_letters) + ' ' + lower_guess + ' \'s in the word.')
            else:
                print('There were no ' + lower_guess + ' \'s in the word.  Try again!')
                count += 1
                hangman_display(count)
                if count == 5:
                    return
            already_guessed.append(lower_guess)
        else:
            print('Invalid guess.  Try again!')
        if display == word:
            print('The word is ' + display + '.')
            print('You won the game!  Congratulations!')
            already_guessed.clear()
            return


main()
