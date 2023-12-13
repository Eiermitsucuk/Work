import random

numbers = list(range(9))
print(numbers)

print("-"*35)
print("Welcome to Battleships Game")
print("-"*35)

board = ["--*--"] * 9
print(board)

def print_board(board):
    print("-"*35)
    line1 = "+".join(board[0:3])
    line2 = "+".join(board[3:6])
    line3 = "+".join(board[6:9])
    print(line1 + "\n" + line2 + "\n" + line3)

print_board(board)


for i in range(3):
    ship = random.choice(numbers)
    numbers.remove(ship)
    board[ship] = "--A--"
    print(ship)

print_board(board)
screen_board = board.copy()

for i in range(4):
    print("-"*35)
    print("", str(4-i))
    guess = int(input(
        """

        0-1-2
        3-4-5
        6-7-8

        Where should we bomb, commander!? =
        """
    ))

    if board[guess] == "--A--":
        print("We hit them !!!")
        screen_board[guess] = "--H--"
    else:
        print("That was close but not enough !!!")
        screen_board[guess] = "--X--"

    print_board(screen_board)

if screen_board.count("--H--") == 3:
    print("They became food for fish")
else:
    print("We lose the war :(")

print("GAME OVER")
