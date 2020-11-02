from classes import Bowler, Player, Team

# A file with helper functions for the main file

# A function which converts a list of names into a list of Player and Bowler instances
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