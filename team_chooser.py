# This file holds the functions which allow the user to choose whether they are using a pre-made team, a
# fully-randomised team or a team the user has named themselves.

import random

from calculator_cricket_oop import team_1, team_2
from cricket_helpers import first_names, team_generator

# Importing lists of male and female names
male_names, female_names = first_names()


# A function for testing the team_generators
def team_holder(team_list):
    team = team_chooser(team_list)
    print(team.players)

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
            return player_made()
        else:
            print('Please enter either "p", "r", or "y".\n')


# Prints the existing premade teams and allows the user to choose betweeen them
def premade(team_list):
    first_team, second_team = team_list
    print('You can choose from the (W)isden XI or the (A)lternate XI:\n')
    print('Wisden XI\t\t\t\t\t\tAlternate XI')
    for player_1, player_2 in zip(first_team.players, second_team.players):
        print(f'{player_1.name:<32}{player_2.name}')
    while True:
        response = input('\n> ').lower()
        if response == 'w':
            print('You have selected the Wisden XI')
            return first_team
        elif response == 'a':
            print('You have selected the Alternate XI')
            return second_team
        else:
            print('Please select either the Wisden XI or the Alternate XI by typing "w" or "a".')


# A holder function for creating randomised teams. First determines the gender of the players, uses this to produce a
# randomised list of players, prints this list for the user to see and then asks them to name the team. Returns the
# generated instance of the Team class.
def randomised():
    gender = determine_gender()
    players = randomise_players(gender)
    print(players)
    team_name = team_namer()
    team = team_generator(players, team_name)
    return team


# A function which allows the user to choose whether they want their team to consist of male players, female players or
# a mixture of both
def determine_gender():
    while True:
        response = input('Would you like a (m)ale team, a (f)emale team, or mi(x)ed?\n> ')
        responses = ['m', 'f', 'x']
        if response in responses:
            return randomise_players(response)


# A function taking in the user's preferred gender, and using this to randomise names from the stored lists of potential
# names
def randomise_players(gender):
    if gender == 'm':
        name_list = male_names['name'].values
    elif gender == 'f':
        name_list = female_names['name'].values
    else:
        name_list = list(male_names['name'].values) + list(female_names['name'].values)
    players = random.choices(name_list, k=11)
    return players


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


# Function which allows the user to enter names for their custom team
def player_made():
    player_list = []
    for i in range(1, 12):
        name = input(f'{i}: ')
        player_list.append(name)
    player_list = confirm_team(player_list)
    team_name = team_namer()
    team = team_generator(player_list, team_name)
    return team


# A function which allows the player to confirm whether they have entered their team correctly and make changes if they
# have made any errors
def confirm_team(player_list):
    while True:
        print("\nYour team:")
        for i, player in enumerate(player_list, 1):
            print(f'{i}: {player}')
        response = input("Is this correct? (y/n)\n> ").lower()
        if response == 'y':
            return player_list
        elif response == 'n':
            return rename_players(player_list)
        else:
            print('Please enter "y" or "n".')


# A function which allows the user to choose whether to rename a specific player or to rename all the players.
def rename_players(player_list):
    while True:
        response = input("Would you like to change a (s)pecific player, or rename (a)ll the players?:\n> ").lower()
        if response == 's':
            return specific_player(player_list)
        elif response == 'a':
            return player_made()
        else:
            print('Please enter "s" or "a".')


# A function which allows the player to index a specific player in the player list and rename them
def specific_player(player_list):
    print("\nYour team:")
    for i, player in enumerate(player_list, 1):
        print(f'{i}: {player}')
    while True:
        response = input("Please enter the player number of the player you would like to rename:\n> ")
        try:
            player_number = int(response) - 1  # Player number will be one larger than the index number
            new_player = input(f'{response}: ')
            player_list[player_number] = new_player
            return player_list
        except TypeError:
            print('Please enter a numeral.')


team_list = [team_1, team_2]

team_holder(team_list)
