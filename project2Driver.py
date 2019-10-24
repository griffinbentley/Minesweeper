from project2 import Minesweeper
playing = True
wins = 0
losses = 0
while playing:
    # While the player still wants to play this asks for user input and gives it to turn()
    height = input("Enter a height: ")
    # Checks to make sure height is valid
    while (not height.isdigit()) or (not 1 < int(height)):
        print("Invalid Input")
        height = input("Enter a height: ")
    length = input("Enter a length: ")
    # Checks to make sure length is valid
    while (not length.isdigit()) or (not 1 < int(height)):
        print("Invalid Input")
        length = input("Enter a length: ")
    numbombs = input("Enter the number of bombs: ")
    # Checks to make sure the number of bombs is valid
    while (not numbombs.isdigit()) or (not 0 < int(numbombs) < int(length)*int(height)):
        print("Invalid Input")
        numbombs = input("Enter the number of bombs: ")
    minesweeper = Minesweeper(int(height), int(length), int(numbombs))
    minesweeper.turn()
    if minesweeper.getWin():
        wins += 1
    else:
        losses += 1
    # Asks the user if they want to play again and if so resets the while loop
    playAgain = input("Do you want to play again (\"yes\" or \"no\")? ")
    print("Win: " + str(wins) + " Lose: " + str(losses))
    while playAgain != "yes" and playAgain != "no":
        print("Invalid Input")
        playAgain = input("Do you want to play again(\"yes\" or \"no\")? ")
    if playAgain == "no":
        playing = False