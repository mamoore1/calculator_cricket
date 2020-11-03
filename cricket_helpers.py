import pandas as pd
from classes import Bowler, Player, Team

# A file with helper functions for the main files

# A function which imports male and female names
def first_names():
    male_names = pd.read_csv('reduced_male_names.csv')
    female_names = pd.read_csv('reduced_female_names.csv')
    return male_names, female_names

# A function which converts a list of names into a list of Player and Bowler instances.
# Note: don't try and put a list of Players in here
def player_converter(name_list):
    player_list = []
    for player in name_list[:7]:
        player_list.append(Player(player))

    for bowler in name_list[7:]:
        player_list.append(Bowler(bowler))

    return player_list

# A function which takes in a list of players and, using player_converter and the Team class, turns them into a team
def team_generator(name_list, team_name):
    player_list = player_converter(name_list)
    team = Team(player_list, team_name)
    return team