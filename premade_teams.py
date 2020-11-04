# PREMADE TEAMS
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