# A file containing functions allowing the user to make their own team, including naming their players.
from cricket_helpers import confirm_team, print_players, team_generator, team_namer


# Function which allows the user to enter names for their custom team, confirm that they are happy with the names, and
# name and generate a team
def user_made():
    player_list = player_namer()
    player_list = confirm_team(player_list, rename_players)
    team_name = team_namer()
    print_players(player_list, team_name)
    team = team_generator(player_list, team_name)
    return team


# A function which allows the user to enter name for their custom players
def player_namer():
    player_list = []
    print('Please enter the full name of your player:\n')
    for i in range(1, 12):
        name = input(f'{i}: ')
        player_list.append(name)
    return player_list

# A function which allows the user to choose whether to rename a specific player or to rename all the players.
def rename_players(player_list):
    while True:
        response = input("Would you like to change a (s)pecific player, or rename (a)ll the players?:\n> ").lower()
        if response == 's':
            return specific_player(player_list)
        elif response == 'a':
            return player_namer()
        else:
            print('Please enter "s" or "a".')


# A function which allows the player to index a specific player in the player list and rename them
def specific_player(player_list):
    print_players(player_list)
    while True:
        response = input("Please enter the player number of the player you would like to rename:\n> ")
        try:
            player_number = int(response) - 1  # Player number will be one larger than the index number
            new_player = input(f'{response}: ')
            player_list[player_number] = new_player
            return player_list
        except ValueError:
            print('Please enter a numeral.')