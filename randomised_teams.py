# RANDOMISED TEAMS: a file holding functions for randomly generating teams
import random

from cricket_helpers import confirm_team, names, print_players, team_generator, team_namer

# Defining player first names and surnames:
male_names, female_names, surnames = names()


# A holder function for creating randomised teams. First determines the gender of the players, uses this to produce a
# randomised list of players, prints this list for the user to see and then asks them to name the team. Returns the
# generated instance of the Team class.
def randomised():
    gender = determine_gender()
    players = randomise_players(gender)
    players = confirm_team(players, gender_and_players)
    team_name = team_namer()
    print_players(players, team_name)
    team = team_generator(players, team_name)
    return team


# A function which allows the user to choose whether they want their team to consist of male players, female players or
# a mixture of both
def determine_gender():
    while True:
        response = input('Would you like a (m)ale team, a (f)emale team, or mi(x)ed?\n> ')
        responses = ['m', 'f', 'x']
        if response in responses:
            player_list = randomise_players(response)
            print_players(player_list)
            return player_list


# A function taking in the user's preferred gender, and using this to randomise names from the stored lists of potential
# names
def randomise_players(gender):
    if gender == 'm':
        name_list = male_names['name'].values
    elif gender == 'f':
        name_list = female_names['name'].values
    else:
        name_list = list(male_names['name'].values) + list(female_names['name'].values)
    player_first_names = random.choices(name_list, k=11)
    player_surnames = random.choices(surnames, k=11)
    players = []
    for first_name, surname in zip(player_first_names, player_surnames):
        players.append(f'{first_name} {surname}')
    return players


# A function which bundles together the determine_gender and randomise_players functions so that they can be called
# together in the confirm_team function. Takes the *args parameter because confirm_team sometimes needs to pass a 
# parameter
def gender_and_players(*args):
    gender = determine_gender()
    player_list = randomise_players(gender)
    return player_list
