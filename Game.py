import random as rn
print("Welcome to the greatest hangman game ever!")

# To figure out
# how to keep the game



#variables
word = "swimming pool"
word_as_a_list = list(word)
word_as_dashes = list("-"*(len(word)))
already_guessed = []
letters_left = []
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number_of_guess_attempts = 7
number_of_tries = 0
has_the_game_ended = "False"

def no_mistakes_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |          ")
    print("   |          ")
    print("   |          ")
    print("   |          ")
    print("-------       ")

def one_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |          ")
    print("   |          ")
    print("   |          ")
    print("-------       ")

def two_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |         | ")
    print("   |         | ")
    print("   |          ")
    print("-------       ")

def three_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |        \| ")
    print("   |         | ")
    print("   |          ")
    print("-------       ")

def four_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |        \|/ ")
    print("   |         | ")
    print("   |          ")
    print("-------       ")

def five_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |        \|/ ")
    print("   |         | ")
    print("   |        / ")
    print("-------       ")

def six_mistake_drawing():
    print('   -----------')
    print("   |         |")
    print("   |         |")
    print("   |        ( ) ")
    print("   |        \|/ ")
    print("   |         | ")
    print("   |        / \ ")
    print("-------       ")

#can I watch my program go through a function in the debugger?
def guessing_func():
    guessed_word = input("Would you like to guess the word right now? Input guess or type 'no'")
    global number_of_tries
    if guessed_word == word:
        print("Well done, you guessed it!")
        # has_the_game_ended == "True"
    elif guessed_word == "no":
        return print("Ok, back to guessing letters")
    elif guessed_word != word:
        return print('Sorry that is not it, another try has been added')
        number_of_tries += 1
while True:
    print("--"*80)
    print("Your current number of tries is {}".format(number_of_tries))
    number_of_tries_left = number_of_guess_attempts-number_of_tries
    print("You have {} tries left".format(number_of_tries_left))
    print("Your current status is {}".format(word_as_dashes))
    def update_drawing():
        if number_of_tries == 0:
            print(no_mistakes_drawing())
        elif number_of_tries ==1:
            print(one_mistake_drawing())
        elif number_of_tries ==2:
            print(two_mistake_drawing())
        elif number_of_tries ==3:
            print(three_mistake_drawing())
        elif number_of_tries == 4:
            print(four_mistake_drawing())
        elif number_of_tries == 5:
            print(five_mistake_drawing())
        elif number_of_tries == 6:
            print(six_mistake_drawing())
    update_drawing()
    def checking_to_see_what_try_you_are_on():
        if number_of_tries_left == 1:
            last_try = input("You have one try remaining, now please guess the word: ")
            if last_try == word:
                print("Well done, you got it on the last try!")
            else:
                print("Sorry you didn't guess the word in time")
    if number_of_tries_left == 1:
        checking_to_see_what_try_you_are_on()
        break
    guessing_func()
    # print(has_the_game_ended)
    update_drawing()
    if number_of_tries_left == 1:
        checking_to_see_what_try_you_are_on()
        break
    chosen_letter = input("Please choose a letter ") #is this what is keeping me from making the line below an elif? Does it always have to be in a line?
    if chosen_letter in already_guessed:
        print("You have already guesssed that please choose another letter")
        continue
    elif chosen_letter in word:
        print("Good guess {} is in the word!".format(chosen_letter))
        already_guessed.append(chosen_letter)
        indices = []
        for i in range(len(word_as_a_list)):
            if word_as_a_list[i] == chosen_letter:
                indices.append(i)
        for l in indices:
            word_as_dashes[l] = chosen_letter
        continue
    elif chosen_letter not in word:
        print("Sorry {} is not in the word, another try has been added".format(chosen_letter))
        number_of_tries += 1
        already_guessed.append(chosen_letter)
        continue
    elif chosen_letter not in alphabet:
        print("Sorry that is an invalid input. Please try again.")
        continue

print("Thank you for playing")