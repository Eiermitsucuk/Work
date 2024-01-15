from word_list import word_dict_easy,word_dict_normal ,word_dict_hard , vowels, animation, word_dict, instructiones, word_dict_very_hard
import random
import time
   
def main(): #main menu
    while True:
        choice = input("\n1.Play\n\n2.How to play\n\n3.Quit\n\n\n:")
        if choice == "1":
            difficulty()
        elif choice == "3":
            print("\n\n\n\n\n\n\n\n\nquitting game...")
            break
        elif choice == "2":
            HowToPlay()
        else:
            print("please type 1, 2 or 3")
            time.sleep(2)
 
def game(word_dict):
    word = random.choice(word_dict) #picks random word from a word_list.py file
    word = " ".join(word).upper() #gives the word space and turns all letters uppercase
    unknown_word = ""
    revealed_letters = ""
    if gamemode == "very_hard":
        guesses = 4 
    else: 
        guesses = 7 #guess amount
    
    while guesses > 0: #loop that counts lifes
        guesses -= 1
        if gamemode == "very_hard":
            VHhangman(guesses)
        else:hangman(guesses)
        for letter in word:  #loops that creates the looked for word
            if letter in vowels:
                unknown_word = unknown_word + letter + " "
            elif letter in revealed_letters:
                unknown_word = unknown_word + letter + " "
            elif letter == " ":
                unknown_word = unknown_word
            else:
                unknown_word = unknown_word + "_ "
        print(unknown_word) #displays the looked for word
        if unknown_word == word + " ": #checks if inputed word matches to searched word
            win()
        letter_guess = input("Guess a letter:")
        if letter_guess.upper() in word and letter_guess.upper() not in vowels and letter_guess.upper() not in revealed_letters: #checks if the letter is correct
            guesses += 1
        print("___________________________________\n")
        letter_guess = letter_verification(letter_guess.upper(), revealed_letters,word.lower().replace(' ', ''))
        if letter_guess == "1":
            guesses += 1
        elif letter_guess == "2":
            guesses += 0
        else:
            revealed_letters = revealed_letters + letter_guess.upper() #keeps a track of all the letters that were alr picked
        print("\n" + str(guesses) + " guesses remaining")
        print("Letters tried: " + ", ".join(revealed_letters))    
        unknown_word = ""
    lost(word)

def letter_verification(letter_guess, revealed_letters,word): 
    if letter_guess.upper() == word.upper():
        win()
    elif letter_guess == "HINT": #hint
        print("Hint:" + "\033[92m " + word_dict.get(word) + "\033[0m")
        letter_guess = "1"
        return letter_guess
    elif len(letter_guess) != 1: #checks the letter count
        print("\033[91m" + "word was not correct" + "\033[0m")
        letter_guess = "2"
        return letter_guess
    elif letter_guess in vowels: #is it a vowel?
        print("\033[91m" + "all vowels are already shown.." + "\033[0m")
        letter_guess = "1"
        return letter_guess
    elif letter_guess in revealed_letters: #was it alr picked?
        print("\033[91m" + "you already tried this letter" + "\033[0m")
        letter_guess = "1"
        return letter_guess
    elif letter_guess.isalpha(): #is it even a letter?
        return letter_guess
    else:
        print("\033[91m" + "only letters please!!" + "\033[0m")
        letter_guess = "1"
        return letter_guess
    
def win():
    print("\033[93m" + "you win woohooo!!!" + "\033[0m")
    print("___________________________________\n")
    time.sleep(2)
    play_again()

def lost(word):
    print(animation[7])
    print("\033[93m" + "you lose, womp womp " + "\033[0m" "\nthe word was... " "\033[36m" +  word + "\033[0m")
    print("___________________________________\n")
    time.sleep(2)
    play_again()

def play_again():
    while True:
        choice = input("\n1.Play again\n\n2.How to play\n\n3.Quit\n\n\n:")
        if choice == "1":
            difficulty()
        elif choice == "3":
            print("quitting game...")
            break
        elif choice == "2":
            HowToPlay()
        else:
            print("please type 1, 2 or 3")
            time.sleep(2)

def difficulty():
    while True:
        difficulty_choice = input("\nchoose difficulty\n\n  1.easy\n\n  2.normal\n\n  3.hard\n\n:")
        global gamemode
        gamemode = ""
        if difficulty_choice == "1":
            gamemode = "easy"
            game(word_dict_easy)
        elif difficulty_choice == "2":
            gamemode = "normal"
            game(word_dict_normal)
        elif difficulty_choice == "3":
            gamemode = "hard"
            game(word_dict_hard)
        elif difficulty_choice == "4":
            gamemode = "very_hard"
            game(word_dict_very_hard)
        else:
            print("\n\n\n\n\n please type 1, 2 or 3\n\n\n\n")
            time.sleep(2)

def hangman(guesses):
    if guesses == 6:
        print(animation[0])
    elif guesses == 5:
        print(animation[1])
    elif guesses == 4:
        print(animation[2])
    elif guesses == 3:
        print(animation[3])
    elif guesses == 2:
        print(animation[4])
    elif guesses == 1:
        print(animation[5])
    elif guesses == 0:
        print(animation[6])

def HowToPlay():
    print(instructiones[0])
    time.sleep(5)
    main()

def VHhangman(guesses):
    if guesses == 3:
        print(animation[0])
    elif guesses == 2:
        print(animation[2])
    elif guesses == 1:
        print(animation[5])
    elif guesses == 0:
        print(animation[6])

if __name__ == "__main__":
    main()