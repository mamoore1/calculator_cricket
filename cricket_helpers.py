import pandas as pd
from classes import Bowler, Player, Team

# A file with helper functions for the main files


# A function which allows the user to confirm whether they are happy with their chosen team. Takes a list of players and
# the function that will allow the user to modify them
def confirm_team(player_list, change_function, team_name='Your team'):
    while True:
        print(f"\n{team_name}:")
        for i, player in enumerate(player_list, 1):
            print(f'{i}: {player}')
        response = input("Are you happy with these players? (y/n)\n> ").lower()
        if response == 'y':
            return player_list
        elif response == 'n':
            player_list = change_function(player_list)
        else:
            print('Please enter "y" or "n".')


# A function which imports male and female names
def names():
    male_names = pd.read_csv('reduced_male_names.csv')
    female_names = pd.read_csv('reduced_female_names.csv')
    surnames = pd.read_csv('surnames.csv')
    surnames_list = surnames['SURNAME'].values
    surnames_title_list = [surname.title() for surname in surnames_list]
    return male_names, female_names, surnames_title_list


# A function which converts a list of names into a list of Player and Bowler instances.
# Note: don't try and put a list of Players in here
def player_converter(name_list):
    player_list = []
    for player in name_list[:7]:
        player_list.append(Player(player))
    for bowler in name_list[7:]:
        player_list.append(Bowler(bowler))
    return player_list


# A function which prints a team's players together with their order in the team. Optional argument allows for team name
# to be entered
def print_players(player_list, team_name='Your team'):
    print(f"\n{team_name}:")
    for i, player in enumerate(player_list, 1):
        print(f'{i}: {player}')


# A function which takes in a list of players and, using player_converter and the Team class, turns them into a team
def team_generator(name_list, team_name):
    player_list = player_converter(name_list)
    team = Team(player_list, team_name)
    return team


# A function which asks the user whether they want to name their own team, or choose from several randomised team
# names
def team_namer():
    print("Would you like to (n)ame your team, or would you like a (r)andomised name?")
    while True:
        response = input('> ').lower()
        if response == 'n':
            return user_name_team()
        elif response == 'r':
            print('randomised')
        else:
            print('Please enter "n" or "r":')


# A function which allows the user to enter a name for their team and confirm that they have entered it correctly
def user_name_team():
    while True:
        team_name = input('Please enter a name for your team:\n> ')
        print(f'You have entered {team_name}.')
        response = input('Is this correct? (y/n)\n> ').lower()
        if response == 'y':
            return team_name
