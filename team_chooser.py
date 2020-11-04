# This file holds the functions which allow the user to choose whether they are using a pre-made team, a
# fully-randomised team or a team the user has named themselves.


from calculator_cricket_oop import team_1, team_2  # For testing purposes
from premade_teams import premade
from randomised_teams import randomised
from user_made import user_made


# A function for testing the team_generators
def team_holder(team_list):
    team = team_chooser(team_list)


# Function for allowing the player to choose players for their team. Using player input, it determines whether to run
# the functions for producing premade, randomised or player made teams.
def team_chooser(team_list):
    while True:
        answer = input('Would you like to choose a (p)remade team, a (r)andomised team, or '
                       '(y)our own team?\n> ').lower()
        if answer == 'p':
            return premade(team_list)
        elif answer == 'r':
            return randomised()
        elif answer == 'y':
            return user_made()
        else:
            print('Please enter either "p", "r", or "y".\n')


team_list = [team_1, team_2]

team_holder(team_list)
