# functionsAreUs
Project 2 for IS303. As a group and using Git/Github, write a program that plays the women’s soccer season as defined in Assignment 4. Modify the code to use functions.

1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message. Return the name to the main program and store it in variable so it can be used throughout the program.

2. Display of menu and return choice. Store in variable and use this value to determine which function to call next.

    Menu will be:
   1. Add home team
   2. Add opponents
        (This will ask for number of games and a team for each one)
   3. Generate scores
   4. Quit

4. Display list of all teams and allow the user to choose a team using a menu. Call the function again to let the user choose the opponent but do not display the team they chose previously. Remove that team from the list. Allow the user to select an opponent, and return team name. This function should receive a parameter but give it a default value if none is passed. You can use this function for both choosing the home team and the opponent team.

5. Play the game receiving both team names. Generate random scores without ties. Return W or L.

6. Display the final record for a team. Receive the home team data and display information.
