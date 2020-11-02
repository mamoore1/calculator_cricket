# This file is defining the classes for use in the main functions

# Defining the Player class. The Player class stores the Player's name, batting score and whether or not they are out.
class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.out = False

    def __repr__(self):
        return self.name


# Defining the Bowler class. As Bowlers are a subset of Players, the Bowler class inherits from the Player class, but
# Additionally keeps track of the Bowlers current wickets and how many runs have been scored off them.
# It also stores bowling style, but this feature has not yet been instantiated
class Bowler(Player):
    def __init__(self, name):
        super().__init__(name)
        self.bowling_style = None
        self.bowler_score = 0
        self.bowler_wickets = 0


# Defining the Team class. The team class keeps track of a list of players, the name of the team, the team's score in runs,
# how many wickets they've lost and which players are bowlers. It also keeps track of whether they are the second team
# to bat, which is used in the match function to determine whether or not there is a score they are trying to beat
class Team():
    def __init__(self, players, team_name):
        self.players = list(players)
        self.name = team_name
        self.score = 0
        self.outs = 0
        self.bowlers = players[7:]
        self.second_innings = False

    def __repr__(self):
        return self.team_name