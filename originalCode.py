# IS 303 Section 003
# Blake Pead, Rebecca Braatz, Joaquin Elizalde, Annie Jaynes, and Michael Jones
# P2 - Functions are Us
# Stores team name and score, opponent name and score, and win or loss all in a doctionary
# Generates team scores for each game and the displays all of the information gathered

import random
iGameCount = 0
dictTeams = {}


def generateScores(home, away, game):
    # Generate scores (no ties!)
    iHomeScore = 0
    iAwayScore = 0
    while iHomeScore == iAwayScore:
        iHomeScore = random.randrange(0,11)
        iAwayScore = random.randrange(0,11)
    
    # Determine win or loss and inform user.
    if iHomeScore > iAwayScore:
        dictTeams[f'Game {game + 1}'] = 'W'
        print(f"\n{home} won this game against {away}. The score was {iHomeScore} - {iAwayScore}.")

    else:
        dictTeams[f'Game {game + 1}'] = 'L'
        print(f"\n{home} lost this game against {away}. The score was {iHomeScore} - {iAwayScore}.")


def display_intro():
    # Displays an introduction and prompts for the user's name.
    print("Welcome to the Women's Soccer Season Simulator!")
    print("The Rules: You will choose a team, play a season, and compete against other teams!")
    playerName =  input("Enter your name: ").strip()
    print(f"Hello {playerName}, let's start the season!")
    return playerName

def addTeams():
    teamList = []
    currInput = ""
    # Uses / as the way to exit the loop
    while currInput != "/":
        currInput = input("Add a team name (enter / to finish adding teams): ")
        if currInput != "/":
            teamList.append(currInput)
    return teamList

def chooseTeams(teams):
    # Clear the games in the dictionary to ensure replayability
    dictTeams.clear()

    # Default teams if none are added
    if teams == []:
        teams = ['Stanford', 'Harvard', 'Yale', 'Princeton', 'University of Virginia', 'University of Michigan', 'University of California', 'University of Florida']
    # Select the Home Team
    listTeams(teams)
    bValid = False
    while bValid == False:
        # use 'Try' to ensure that invalid choices don't crash the code
        try:
            iHomeTeam = int(input('Select a home team from the list above (enter list number): '))
            # Grab the team name so it can be re-added after the games are finished (for replayability so team doesnt need to manually be re-added)
            sHomeName = teams[iHomeTeam - 1]
            # Remove home team from list
            teams.pop(iHomeTeam - 1)
            bValid = True
        except:
            print(f'That is not a valid option. Please select a number from the list.')

    #Choose how many games
    bValid = False
    while bValid == False:
        # use 'Try' to ensure that invalid choices don't crash the code
        try:
            iGames = int(input('How many games would you like to simulate? (Please enter a whole number): '))
            bValid = True
        except:
            print('Please enter a whole number.')

    # Select opponents for each game played
    for game in range(iGames):
        listTeams(teams)
        bValid = False
        while bValid == False:
            # use 'Try' to ensure that invalid choices don't crash the code
            try:
                iOpponent = int(input(f'select an opponent for game {game + 1} (enter list number): '))
                # Call the generateScores() function
                generateScores(sHomeName, teams[iOpponent - 1], game)
                bValid = True
            except:
                print(f'That is not a valid option.')
    # Once the game is complete and record is printed, add the home team back into the list so the game can be replayed
    teams.append(sHomeName)
    return sHomeName

# Lists out all of the teams available to choose from in a numbered list
def listTeams(teams):
    # Prints a blank like (for aesthetics)
    print(' ')
    iTeamCount = 1
    for team in teams:
        print(f'{iTeamCount}: {team}')
        iTeamCount += 1

# Function that displays the menu
def displayMenu():
    print("\nMenu:")
    print("1. Add Teams")
    print("2. Generate Scores")
    print("3. Quit")
    try:
        option = int(input("Enter option: "))
        return option
    except:
        return None

# Function that prints the home team and their respective record
def printSummary(sHomeTeam):
    
    # Declares the varibles that will calculate wins and losses
    iWins = 0
    iLoss = 0

    # For Loop to loop through all the results pf games stored in the dictionary dictTeams
    for game, data in dictTeams.items():

        # If data stored is a win, store add one to iWins. Else add one to iLoss
        if data == 'W':
            iWins += 1
        else:
            iLoss += 1

    # PRint the record in the format wins - Losses
    print(f"\n{sHomeTeam}'s final season record: {iWins} - {iLoss}")
    
    #Calculate wins and losses as a percent. Print statement customized based on success
    if iWins / (iWins + iLoss) >= 0.75:
        print("Great Job!")
    elif iWins / (iWins + iLoss) >= 0.5:
        print("You had a good season!")
    else:
        print("Your teams needs to practice!")

# Function 1
display_intro()
choice = 1
newList = []
contMenu = True

# Loops until quit is selected
while contMenu == True:
    # Function 2
    choice = displayMenu()
    if choice == 1:
        newList.extend(addTeams())
    elif choice == 2:
        # Function 3 (Function 4 is inside of this function)
        homeName = chooseTeams(newList)
        # Function 5
        printSummary(homeName)
    # Quits the program
    elif choice == 3:
        print('\nThanks for playing! The program will now close.')
        # Ends the loop
        contMenu = False
    # This is if something is not selected in the list
    else:
        print('\nPlease enter a valid option.')