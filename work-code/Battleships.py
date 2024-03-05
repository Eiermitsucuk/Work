import random
import time

def start_menu():         #starting the game
    print("""
        
             !!!     Welcome to Battleships Game     !!!

             ⠀⠀  ⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡇⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡇⠀⠀⠀⠀⠀⠀⠀⣀⡤⡞⢫⡎⢸⢱⠀⠀⠻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⣟⡒⣶⣶⣶⣾⡯⠟⠛⠁⠈⢳⣼⣸⠀⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠉⠓⠿⣟⣓⣒⣀⡤⠶⠚⠉⢹⣿⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⢿⣶⡗⠒⠒⠒⠒⠲⠶⣶⠶⠶⠦⠼⢿⣦⣀⣀⣀⣀⣀⠀⠀⠈⠳⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠈⢣⡀⠀⠀⠀⠈⠳⣌⠉⠉⠉⠉⠙⢿⡷⠿⢶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠝⢆⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠈⠳⡄⠀⠀⠀⠀⠙⢦⡀⠙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⢧⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠀⠈⢳⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⣧⠀⠀⠀⠀⠀⠀⠈⢣⠀⠀⠀⠀⠀⠈⣦⠀⠀⠀⠀⠀⠹⡀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡆⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠀⠀⢻⡄⠀⠈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⢸⠀⠀⠀⠀⠀⠀⠸⣦⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠈⢧⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠘⡆⠀⡆⠀⠀⠀⠀⡟⡇⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⢸⣆⠀⠀⠀⠀⠹⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⡇⡀⢰⠀⠀⠀⠀⣷⠃⡇⢠⡄⠀⠀⢸⢸⢠⡄⠀⠘⡟⣿⠀⠀⠀⠀⠀⢸⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠟⡿⠀⢸⢀⢀⠀⢠⡟⡔⡇⡌⡇⠀⠀⣺⢸⢸⣿⣰⢀⣧⡿⠀⠀⠀⣀⣴⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣤⠤⢤⣤⣾⠀⡇⡀⡌⣼⣼⠀⣴⣿⡇⡇⣿⡇⡆⣀⣿⣿⣸⢹⣿⢸⣿⠀⢰⠒⠾⣿⣻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢿⡞⠛⣻⣿⣟⡛⠛⣻⡇⢸⢁⣿⡇⣿⣇⣤⣿⣿⢳⣿⢻⢳⣿⣹⣏⡇⣯⣿⠃⣼⣾⡤⢾⠁⠈⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣾⣷⣲⣾⣿⣶⣾⢁⡞⣾⣾⣻⣿⣽⣿⠟⣏⣎⡟⣞⣾⣿⣿⢹⣼⣹⣿⣴⠟⠉⠀⣾⠀⢰⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⢯⣿⣿⣿⣻⣿⠃⡼⣹⢳⣿⣿⣽⣿⣿⣾⡘⣹⣽⣻⡿⣿⣣⣷⡿⠛⢻⡾⠷⣄⢀⣿⠀⢸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡷⠶⠯⠿⣭⡾⢃⡞⣱⢟⣿⣿⣿⣻⣤⣤⣽⣿⡷⣧⣽⡿⢟⣉⡁⠀⠀⢨⢿⣶⣿⣿⠇⢀⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣤⣼⣷⣤⣤⣼⣿⣗⣾⣤⣽⣊⣿⣿⣿⣿⢯⡤⠿⣿⣿⣿⡼⠷⠈⢃⣠⣤⣶⣿⣿⣿⢿⣿⠀⣸⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣍⠉⢹⣿⡿⣿⣿⠿⠿⠛⠛⢹⣯⢹⣿⡟⣆⢸⠿⣠⣿⣿⣻⠧⠖⠛⣿⠖⠋⣽⣿⢽⣶⣿⠣⣶⣿⠃⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣼⣿⣷⣿⣿⣶⣄⣀⣀⣀⣠⣤⣿⣿⠛⠿⠿⣛⣻⡷⠋⠀⠐⠀⣿⣶⢾⣿⠟⣫⢴⠏⢠⣿⢻⣧⣴⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣤⣀⠀⠀⢀⣀⡉⠉⠉⠛⢛⣛⣿⠿⣿⣶⣾⣿⣩⣅⡤⠶⠶⠛⠉⠙⠛⣿⣛⣭⠏⢠⣿⠻⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣟⡛⠛⠓⠒⠲⠲⠾⠿⠿⠿⠿⠛⠛⠛⠛⠛⠉⠁⠀⣀⣀⣠⣴⣞⡿⢽⣿⠃⣰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠹⣿⡦⣄⣠⣠⣦⣤⣀⣀⣀⣀⣀⣀⣀⣤⣤⡤⠤⠶⠿⠛⣋⣿⣷⣶⡿⡥⣶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡿⠋⣼⠿⣻⡿⣿⣻⣟⣦⣄⣀⣠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣲⣾⣿⣟⣿⣿⠋⣠⣾⠯⢤⣄⡀⠀⢀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣁⢸⡇⠈⣇⠀⣿⠛⣦⠙⢪⣷⠿⠛⠓⠒⠾⠷⣶⡶⠶⠶⢶⣶⣶⣶⣶⣟⣹⣯⣷⠞⢁⣴⠿⢿⡶⣄⡉⠟⣿⡍⠉⣙⡻⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢿⢿⠇⢿⣄⠘⠳⠽⠷⢯⡀⢹⣇⠀⠀⣀⡤⠤⠤⢤⣈⡛⢶⣞⠁⢀⣀⠀⠉⠻⠟⠡⠴⠛⠛⠛⠋⠛⢳⣍⠀⠹⣿⡄⠈⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣶⣤⣤⣼⠇⠈⠻⣦⣀⢹⣷⣶⠀⠀⠈⠉⠛⢿⣦⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⢀⣾⡿⠣⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠀⠀⠀
        """)
    print("1. Play Game")
    print("2. View Highscores")
    print("3. Exit")
    print("-" * 45) 

def print_board(board):
    rows = len(board)
    columns = len(board[0]) #this both code calculates the number of rows and columns

    print("  " + " ".join([str(i) for i in range(0, columns + 1)]))
     #this function prints the contents, which is represented as a list.

    for i, row in enumerate(board):
        print(f"{chr(ord('A') + i)} {' '.join(row)}")
    #this generates a sequence of numbers. then it adds each number to the "(ord("A"))" and then converts it again to a character by writing "chr()"



def create_board(rows, columns):
    return [[" " for _ in range(columns)] for _ in range(rows)] #this function creates the gameboard automatically

def letter_to_index(letter): 
    return ord(letter) - ord("A")

 # takes the uppercase letter as inout and returns its index in the alphabet. It calculates the index by subtracting the ASCII.
 #ASCII means "American Standard Code fo Information Interchange". It assigns a unique number to each charactersv (letters, numbers or symbols)

def save_highscores(score):
    with open("battleships_highscores.txt", "a") as file:
        file.write(f"{player}: {score}\n")

 #saves the score to file. "with" and "a" is for opening the file in append mode and it writes the new scores on new lines by writing "\n". 

def view_highscores():
    print("Highscores:")
    try:
        with open("battleships_highscores.txt", "r") as file: # "with" and "r" stands for to make sure the file is closing after reading
            highscores = file.readlines()
            if not highscores:
                print("There is no highscores saved yet.")
            else:
                for idx, score in enumerate(highscores, start=1):
                    print(f"{idx}. {int(score)}")
    except FileNotFoundError:
        print("There is no highscores saved yet.")
 
 #this function reads and displays the highscores stored in the file

def play_game():
    player = input("Enter your username: ")
    score = 0
    rows = 10
    columns = 10
    board = create_board(rows, columns)

    for i in range(4):
        ship_row = random.randint(0, len(board) - 1) #this generatesa random index within the range of valid indices on the board.
        ship_col = random.randint(0, len(board[0]) - 1) # does the same thing but for columns instead of rows
        board[ship_row][ship_col] = '0' # this one assigns "0" to the cell by the randomly generated row and column indices

    print_board(board)
    screen_board = [[' ' for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(5):
        print("-" * 45)
        print("", str(5 - i))

        while True:
            try:
                guess = input(" Where should we bomb, commander!? (Enter coordinates, e.g., A1): ")
                guess_index = letter_to_index(guess[0]), int(guess[1])

                if 0 <= guess_index[0] < len(board) and 0 <= guess_index[1] < len(board[0]): #this checks if the guessed row/column index is more or equal to 0 and less than the total number of rows and columns in the baord.
                    break
                else:
                    print("Invalid input. Please enter valid coordinates.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

        if board[guess_index[0]][guess_index[1]] == '0':
            print("We hit them !!!")
            screen_board[guess_index[0]][guess_index[1]] = "H"
            score += 1
        else:
            print("That was close but not enough !!!")
            screen_board[guess_index[0]][guess_index[1]] = "X"

        print_board(screen_board)
        time.sleep(2)

    if sum(row.count("H") for row in screen_board) == 4:
        print("They became food for fish")
    else:
        print("We lost the war :(")

    save_highscores(f"{player}: {score}") # in this code "f" will replace "player" and "score" with their value of the variable and will result in a string that shows the player's name and score together

    return score
2
def main():
    score = 0
    while True:
        start_menu()
        choice = input("Enter your choice (1, 2 or 3.): ")

        if choice == "1":
            score = play_game()
        elif choice == "2":
            view_highscores()
        elif choice == "3":
            print("Exiting game")
            break
        else:
            print("Invalid choice. Enter 1 to play, 2 to view highscores and 3 to exit.")

    print(f"Your score: {score}")
    save_highscores(score)
    print("GAME OVER")

if __name__ == "__main__":
    main()