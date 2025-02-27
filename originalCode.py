# Stores team name and score, opponent name and score, and win or loss all in a doctionary
# Generates team scores for each game and the displays all of the information gathered

import random
iGameCount = 0
dictTeams = {}
iWins = 0
iLoss = 0

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
        print(f"{home} won this game against {away}. The score was {iHomeScore} - {iAwayScore}.")

    else:
        dictTeams[f'Game {game + 1}'] = 'L'
        print(f"{home} lost this game against {away}. The score was {iHomeScore} - {iAwayScore}.")


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
    while currInput != "/":
        currInput = input("Add a team name (enter / to finish adding teams): ")
        if currInput != "/":
            teamList.append(currInput)
    return teamList

def chooseTeams(teams):
    # Clear the games in the dictionary to ensure replayability
    dictTeams.clear()

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

# Lists out all of the teams available to choose from in a numbered list
def listTeams(teams):
    iTeamCount = 1
    for team in teams:
        print(f'{iTeamCount}: {team}')
        iTeamCount += 1

# Function that displays the menu
def displayMenu():
    print("Menu:")
    print("1. Add Teams")
    print("2. Generate Scores")
    print("3. Quit")
    option = int(input("Enter option: "))
    return option

display_intro()
choice = 1
newList = []

while choice == 1:
    choice = displayMenu()
    if choice == 1:
        newList.extend(addTeams())

if choice == 2:
    chooseTeams(newList)


# Stores everything in the dictionary and determines win or loss

    # dictTeams[f'Game {game + 1}'] = {
    #     'HomeName': sHomeTeam,
    #     'HomeScore': iHomeScore,
    #     'OppName': sAwayTeam,
    #     'AwayScore': iAwayScore
    # }

# At the end of the season, prints the results of each game and final ratio of home team

print('')
for game, data in dictTeams.items():
    print(f"{game}:\n{data['HomeName']}'s score: {data['HomeScore']}, {data['OppName']}'s score: {data['AwayScore']}.")
    if data['Win'] == 'W':
        iWins += 1
    else:
        iLoss += 1

print(f'\nFinal season record: {iWins} - {iLoss}')

# Prints out final message based on the ratio

if iWins/iSeasonGames >= 0.75:
    print("Qualified for the NCAA Women's Soccer Tournament!\n")
elif iWins/iSeasonGames >= 0.5:
    print('You had a good season.\n')
else:
    print('Your team needs to practice!\n')