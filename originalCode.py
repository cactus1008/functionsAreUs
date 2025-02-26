# Stores team name and score, opponent name and score, and win or loss all in a doctionary
# Generates team scores for each game and the displays all of the information gathered

def generateScores(home, away):
    # Generate scores (no ties!)
    iHomeScore = 0
    iAwayScore = 0
    while iHomeScore == iAwayScore:
        iHomeScore = random.randrange(0,11)
        iAwayScore = random.randrange(0,11)
    
    # Determine win or loss and inform user.
    if iHomeScore > iAwayScore:
        dictTeams[f'Game {game + 1}']['Win'] = 'W'
        print(f"You won this game against {away}. The score was {iHomeScore}:{iAwayScore}.")

    else:
        dictTeams[f'Game {game + 1}']['Win'] = 'L'
        print(f"You lost this game against {away}. The score was {iHomeScore}:{iAwayScore}.")

import random
iGameCount = 0
dictTeams = {}
iWins = 0
iLoss = 0

# Get team name and number of games played

sHomeTeam = input("Enter your Home Team's name: ")
iSeasonGames = int(input(f"Enter how many games {sHomeTeam} will play in their season (enter a number): "))

# Loop each game to get opponent name

for game in range(iSeasonGames):
    sAwayTeam = input(f"Enter the name of the away team for game {iGameCount + 1}: ")
    iGameCount += 1


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