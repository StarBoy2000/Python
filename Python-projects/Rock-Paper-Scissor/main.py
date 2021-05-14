# importing required modules
from logging import exception
from mysql.connector.errors import Error
import packages.connect
import packages.rules
import packages.game
import packages.clear
import sys


# defining main function to call the other modules
def main():

    # check connectivity with the SQL server
    packages.connect.connectivity()

    # clearing the existing values in the database or not
    packages.clear.clearData()

    # display the game rules
    packages.rules.gameRules()

    # call main logic of the game
    packages.game.mainLogic()

# call main function
try:
    main()
except:
    while True:
        print("\nPlease check your connection with the MySQL Server!")
        tryAgain = input("\nTry Againg? (y/n): ").lower()
        if tryAgain not in ('y','n'):
            print("Invalid input!")
            continue
        if tryAgain == 'y':
            main()
        else:
            print("GoodBye!")
            False
            break