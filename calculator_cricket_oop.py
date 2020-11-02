# Importing libraries

import random
import pandas as pd

from classes import Bowler, Player, Team
from cricket_helpers import team_generator
# Importing lists of names for randomised teams.

male_names = pd.read_csv('reduced_male_names.csv')
female_names = pd.read_csv('reduced_female_names.csv')

# Pre-defining two possible teams for testing

first_team = ['Jack Hobbs', 'WG Grace', 'Donald Bradman', 'Sachin Tendulkar', 'Viv Richards', 'Garry Sobers', 'Alan Knott', 'Wasim Akram', 'Shane Warne', 'Malcolm Marshall', 'Sydney Barnes']
second_team = ['Herbert Sutcliffe', 'Sunil Gavaskar', 'Ricky Ponting', 'Brian Lara', 'Jacques Kallis', 'Graeme Pollock', 'Adam Gilchrist', 'Imran Khan', 'Dennis Lillee', 'Muttiah Muralitharan', 'Jim Laker']

# Defining the two teams using the team_generator helper function

team_1 = team_generator(first_team, 'Wisden XI')
team_2 = team_generator(second_team, 'Alternate XI')

# Defining the function which holds the functions making up the rest of the game
def app_handler(first_team, second_team):
    input('Welcome to Mike\'s Calculator Cricket game! Press enter to start.\n')
    print('Today\'s match is between ' + str(first_team) + ' and ' \
          + str(second_team) + '. It looks like both sides are ready to begin and the captains are ready for the coin toss.')
    bat_first, bowl_first = coin_toss(first_team, second_team)
    input('\nWe\'re ready for the first ball of the match. {opener1} and {opener2} are opening for {team1} and {bowler} is opening the bowling for {team2}.\n\nPress enter to start\n'.format(\
                  opener1 =  bat_first.players[0], opener2 = bat_first.players[1],\
                      team1 = str(bat_first), team2 = str(bowl_first), bowler =\
                          bowl_first.bowlers[-1]))
    innings(bat_first, bowl_first)
    bowl_first.second_innings = True
    input('\n{team2} are up to bat and they need to beat {runs}. {opener1} and {opener2} will be opening the batting for {team2}, while {bowler} is opening the bowling. Press enter to continue\n'.format(team2 = str(bowl_first), runs = bat_first.score, opener1 = bowl_first.players[0], opener2 = bowl_first.players[1], bowler = bat_first.bowlers[-1]))
    innings(bowl_first, bat_first)
    winning_side(bat_first, bowl_first)
    input('Press enter to quit')


# Choosing which team wins the coin toss. The player can choose whether to bat or bowl
# while the computer always bats
def coin_toss(first_team, second_team):
    coin_result = random.choice(['heads', 'tails']) # Generating coin toss
    while True:
        coin_call = input('\n(heads) or (tails)?\n> ').lower()
        if coin_call in ['heads', 'tails'] and coin_call == coin_result: # Player wins the toss
            print(f'\nThe coin has come up {coin_result}.')
            print(f'{first_team} has won the toss.\n')
            choice = bat_or_bowl(first_team, second_team) # Function returns order of batting and bowling teams
            return choice
        elif coin_call in ['heads', 'tails'] and coin_call != coin_result: # Player loses toss
            print(f'\nThe coin has come up {coin_result}.')
            print(f'{second_team} has won the toss and elected to bat.\n')
            return second_team, first_team
        elif coin_call not in ['heads', 'tails']:
            print('Please type either \'heads\' or \'tails\'.\n')
 
# Function which asks the player to choose whether to bat or bowl
def bat_or_bowl(first_team, second_team):
    while True:
        choice = input('\n(bat) or (bowl)?\n> ').lower()
        if choice == 'bat':
            return first_team, second_team
        elif choice == 'bowl':
            return second_team, first_team
        else:
            print('Please type either \'bat\' or \'bowl\'.')

# Function generating 6 random numbers between 0 and 9. If an 8 is generated, 
# this is classified as a no-ball and an extra ball is generated. This function
# returns the list of scores, which are evaluated in the innings function
def over_generator():
    over = []
    no_balls = 0
    for i in range(6):
        ball = random.sample(range(0, 10), 1)[0]
        if ball == 8:
            no_balls += 1
        over.append(ball)
    while no_balls:
        ball = random.sample(range(0, 10), 1)[0]
        over.append(ball)
        if ball != 8:
            no_balls -= 1
    return(over)


# This function takes the order the teams are playing, evaluates the scores 
# returned by the over function and gives scores accordingly.
def innings(team, team2):
    bowler_number = 0 # Keeps track of the current bowling pair, changing them part way through
    over_number = 1
    batsman_switch_counter = 0 # Keeps track of which batsman is currently facing the bowler
    first_batsman = team.players[0] # Defines the opening pair
    second_batsman = team.players[1]
    announce = '{batsman} scores {number} runs.'
    batter_out = '{batsman} goes out with {number} runs!'
    bowling_pair =  [team2.bowlers[-1], team2.bowlers[-2]] # Sets the starting bowlers as the last two players on team2
    
    # Checking that the team are not all out or, if it is the second innings, that the team has not overtaken their opponent
    while team.outs < 10 and not (team.second_innings == True and team.score > team2.score) and over_number < 21:
        if bowler_number % 2 == 0: # Determines which bowler should be bowling
            bowler = bowling_pair[0]
        else:
            bowler =  bowling_pair[1]
        over = over_generator()
        for score in over:
            batting_pair = batsman_picker(first_batsman, second_batsman, batsman_switch_counter) # Determines which of the current batsmen should be facing
            first_batsman = batting_pair[0]
            batsman = first_batsman # Renaming for ease
            second_batsman = batting_pair[1]
            batsman_switch_counter = 0
            if team.second_innings == True and team.score > team2.score:
                print(f'\n{team} have done it! They\'ve caught {team2}!')
                break
            elif team.outs >= 10:
                break
            elif score == 1:
                team.score += score
                batsman_switch_counter = 1
                batsman.score += score
                bowler.bowler_score += score
                print('{} scores 1 run!'.format(batsman.name))
        
            elif score <= 4:
                team.score += score
                batsman.score += score
                bowler.bowler_score += score
                if score == 3:
                    batsman_switch_counter = 1
                print(announce.format(batsman = batsman.name, number = score))
                
            elif score == 6:
                team.score += score
                batsman.score += score
                bowler.bowler_score += score
                print('{batsman} smashes {bowler} for six!'.format(batsman = batsman.name, bowler = bowler))
        
        
            elif score == 5 or 6 < score < 8:
                print(announce.format(batsman = batsman.name, number = 0))
        
            elif score == 8:
                ball = (random.sample(range(2),1)[0])
                if ball == 0:
                    print('No ball!')
                else:
                    print('Wide!')
                team.score += 1
                bowler.bowler_score += 1
            
        
            else:
                team.outs += 1
                bowler.bowler_wickets += 1
                print(wicket_taker(batsman, bowler, team2), 'Out!')
                print(batter_out.format(batsman = batsman.name, number = batsman.score) ,'\n')
                batsman.out = True
                first_batsman = new_batsman(team, batting_pair)
                if team.outs >= 10:
                    print('That\'s the final wicket!')
                
        batsman_switch_counter += 1
        bowler_number += 1
        bowling_pair = bowler_pair(team2, bowler_number) #Determines the new bowling pair
        if bowler_number % 2 == 0:
            bowler = bowling_pair[0]
        else:
            bowler =  bowling_pair[1]
        over_number +=1
        if team.outs < 10 and not (team.second_innings == True and team.score > team2.score):
            print('\n{team} are on {runs} for {wickets} after {overs} overs, {bowler} to bowl.'.format(team = team, runs = team.score, wickets = team.outs, overs = over_number-1, bowler=bowler))
        input('\nPress enter to continue\n\n')
    endgame(team, team2)

# Picks the next batsman from the players who have yet to bat
def new_batsman(team, batting_pair):
    for batter in team.players:
        if batter.out != True and batter not in batting_pair:
            return batter


# Determines the current bowlers based on how far through the game we are.
# At some point I would like to allow the player to choose their next bowler.
def bowler_pair(team2, bowler_number):
    bowler_pair = []
    if bowler_number < 8 or bowler_number >= 16:
        bowler_pair = [team2.bowlers[-1], team2.bowlers[-2]]
    else:
        bowler_pair = [team2.bowlers[-3], team2.bowlers[-4]]
    return(bowler_pair)

# Determines how the wickets was taken, based on the real life statistics for
# how common wicket types are.
def wicket_taker(batsman, bowler, team2):
    wicket_type = random.sample(range(0, 100, 1), 1)[0]
    if wicket_type < 21:
        stump = random.choice(['off-stump', 'middle-stump', 'leg-stump'])
        wicket = f'{bowler} knocks {batsman}\'s {stump} out of the ground!'.format(bowler=bowler, batsman=batsman, stump=stump)
    elif 21 <= wicket_type < 78:
        fielder = random.choice(team2.players)
        wicket = f'{batsman} hits the ball in the air to {fielder}!'
    elif 57 <= wicket_type < 94:
        wicket = f'{batsman} gets hit on the leg in front of the stumps! {bowler} is appealing!'
    elif 94 <= wicket_type < 98:
        wicket = f'{batsman} goes for a quick single but can\'t make it in time!'
    elif wicket_type >= 98:
        wicket = f'{batsman} charges down the wicket but misses, and the keeper is too fast for him!'
    return wicket

# Picks which batsman is currently facing the bowler
def batsman_picker(first_batsman, second_batsman, switch):
    if switch % 2 == 0:
        batsman1 = first_batsman
        batsman2 = second_batsman
    else:
        batsman1 = second_batsman
        batsman2 = first_batsman
    return [batsman1, batsman2]

# Displays the score of the team at the end of the innings, as well as the top batsmen and bowlers
def endgame(team, team2):
    print('The final score is ' + str(team.score) + ' for ' + str(team.outs) + '\n\n')
    bowlers = '{name} {wickets} for {runs}'
    top_scorer(team) # Determines the top scorers
    best_bowlers(team2) # Determines the top bowlers
    print('Performances:')
    for i in range(0, 3):
        print(str(team.top_scorers[i][0]), str(team.top_scorers[i][1]) +\
              '\t\t' + str(bowlers.format(name = team2.top_bowlers[i][0],\
                                          wickets = team2.top_bowlers[i][1],\
                                              runs = \
                                                  (team2.top_bowlers[i][0]).bowler_score)))
    print('\n')
    
def top_scorer(team):
    player_scores = {player: player.score for player in team.players}
    scores = sorted(player_scores.items(), key=lambda kv: kv[1], reverse = True)
    team.top_scorers = scores[0:3]
    
def best_bowlers(team):
    bowler_scores = {bowler: bowler.bowler_score for bowler in team.bowlers}
    bowler_wickets = {bowler: bowler.bowler_wickets for bowler in team.bowlers}
    # Thinking of finding a way to order by scores after ordering by wickets
    sorted_scores = sorted(bowler_scores.items(), key=lambda kv: kv[1], reverse = True)
    sorted_wickets = sorted(bowler_wickets.items(), key=lambda kv: kv[1], reverse = True)
    team.top_bowlers = sorted_wickets[0:3]
    
# Determines and displays who won and lost
def winning_side(first_team, second_team):
    winner = '\n\n{team1} won with {runs} {wickets}, against {team2}\'s {runs2} {wickets2}.'
    draw = 'Both sides drew on {runs}.'
    bowlers = '{name} {wickets} for {runs}'
    
    if first_team.outs == 10:
        first_team_outs = 'all out'
    else:
        first_team_outs = 'for ' + str(first_team.outs)
        
    if second_team.outs == 10:
        second_team_outs = 'all out'
    else:
        second_team_outs = 'for ' + str(second_team.outs)
        
    if first_team.score > second_team.score:
        print(winner.format(team1 = first_team, runs = first_team.score, wickets = first_team_outs, team2 = second_team, runs2 = second_team.score, wickets2 =  second_team_outs))
    elif first_team.score == second_team.score:
        print(draw.format(runs = first_team.score))
    else:
        print(winner.format(team1 = second_team, team2 = first_team, runs = second_team.score, wickets = second_team_outs, runs2 = first_team.score, wickets2 =  first_team_outs))
    
#def top_scorer_each_team(first_team, second_team):
    print('\n\nFirst innings:')
    for i in range(0, 3):
        print(str(first_team.top_scorers[i][0]), str(first_team.top_scorers[i][1]) + '\t\t' + str(bowlers.format(name = second_team.top_bowlers[i][0], wickets = second_team.top_bowlers[i][1], runs = (second_team.top_bowlers[i][0]).bowler_score)))
    
    print('\n\nSecond innings:')
    for i in range(0, 3):
        print(str(second_team.top_scorers[i][0]), str(second_team.top_scorers[i][1]) + '\t\t' + str(bowlers.format(name = first_team.top_bowlers[i][0], wickets = first_team.top_bowlers[i][1], runs = (first_team.top_bowlers[i][0]).bowler_score)))


#app_handler(team_1, team_2)