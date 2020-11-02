# This file holds the functions which allow the user to choose whether they are using a pre-made team, a
# fully-randomised team or a team the user has named themselves.

import random

import pandas as pd

from calculator_cricket_oop import team_1, team_2
from cricket_helpers import team_generator

# Importing lists of male and female names
male_names = pd.read_csv('reduced_male_names.csv')
female_names = pd.read_csv('reduced_female_names.csv')


# Function for allowing the player to choose players for their team
def team_chooser(team_list):
    while True:
        answer = input('Would you like to choose a (p)remade team, a (r)andomised team, or (y)our own team?\n> ').lower()
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


#A holder function for determining
def randomised():
    gender = determine_gender()
    players = randomise_players(gender)
    print(players)
    team_name = team_namer()
    team = team_generator(players, team_name)
    print(team.team_name, team.players, team.bowlers)


# A function which allows the user to choose whether they want their team to consist of male players, female players or
# a mix
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
    return(players)


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
        response = input('Is this correct? (y/n)\n> ')
        if response == 'y':
            return team_name




def player_made():
    pass

team_list = [team_1, team_2]

team_chooser(team_list)