team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
elif team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
if team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")
    
#1 The teams have the same number of wins because team A wins again and therefore ties the score
#2 elif and else are giving options further than what if does so that if the if function is not satisfied there are other options than doing multiple if funtions.
#3 if the elif statement in line 18 is changed to an if statement, nothing changes because the new if statement functions like and elif statement, being another possiblity determined by a variable.