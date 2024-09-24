# Name of the team
team = "Toronto Blue Jays"
# current date
current_date = "July 18, 2021"
# Name of player
player = "Vladimir Guerrero Jr."
# NUmber of home runs the player has done
home_runs_to_date = 31
# NUmber of games player has played in this season
games_played = 88
# Number of games in the season
total_season_games = 162
# Home run record
home_run_record = 73

#The break here seperates the variables from the operators
# games_remaining = total_season_games - games_played is correct because as logn as the variables are correct the number of games remaining is the number of gamesp layed subtracted from teh total number of games in the season
games_remaining = total_season_games - games_played
home_runs_per_game = home_runs_to_date / games_played
projected_home_runs = home_runs_per_game * total_season_games
can_break_record = projected_home_runs > home_run_record

# This break seperates the printing from the operators
print(f"{player} of the {team}")
print(f"currently has {home_runs_to_date} home runs as of {current_date}.")
print(f"The current MLB record for most home runs in a season is {home_run_record}.")
print(f"With {games_remaining} games remaining and an average of {round(home_runs_per_game)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs)} home runs this season.")