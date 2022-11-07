#######################
# part 2 - basic python
#######################

#################
# following along
#################
1 + 1

##########
# comments
##########

# print the result of 1 + 1
print(1 + 1)

###########
# variables
###########

goals_scored = 2

goals_scored
3*goals_scored

goals_scored = goals_scored + 1
goals_scored

####################
# types of variables
####################

penalty_minutes = 15  # int
puck_speed = 82.5  # float

starting_lw = 'David Perron'
starting_c = "Ryan O'Reilly"

type(starting_lw)

type(penalty_minutes)

starters = f'{starting_c}, {starting_lw}, etc.'
starters

# string methods
'do you believe in miracles!?'.upper()

'Bernie Geoffrion'.replace('Bernie', 'Boom Boom')

####################################
# How to figure things out in Python
####################################
foo = 'sidney crosby'  # alt if 'sidnedy crosby'? doesn't work in REPL

'sidney crosby'.capitalize()

'  sidney crosby'
'sidney crosby'

'  sidney crosby'.lstrip()

#######
# bools
#######
team1_goals = 2
team2_goals = 1

# and these are all bools:
team1_won = team1_goals > team2_goals
team2_won = team1_goals < team2_goals
teams_tied = team1_goals == team2_goals
teams_did_not_tie = team1_goals != team2_goals

type(team1_won)
teams_did_not_tie

# error because test for equality is ==, not =
# teams_tied = (team1_pts = team2_pts)  # commented out since it throws an error

shootout = (team1_goals > 4) and (team2_goals > 4)
at_least_one_good_team = (team1_goals > 4) or (team2_goals > 3)
you_guys_are_bad = not ((team1_goals > 1) or (team2_goals > 1))
meh = not (shootout or at_least_one_good_team or you_guys_are_bad)

###############
# if statements
###############
if team1_won:
  message = "Nice job team 1!"
elif team2_won:
  message = "Way to go team 2!!"
else:
  message = "must have tied!"

message

