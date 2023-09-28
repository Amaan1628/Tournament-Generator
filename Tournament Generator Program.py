def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams >= 2 :
            break
        print("The minimum number of teams is 2, try again.")
    return num_teams

def get_team_names(num_teams):
    team_names=[]

    for x in range(num_teams):
        while True:
            team_name = input(f"Enter the name of team #{x + 1}: ")
            num_words = len(team_name.split(" "))
        
            if num_words>2:
                print("team name must have at most 2 words")
            elif len(team_name) < 2:
                print("Team name must have at least 2 characters")
            else:
                break
        team_names.append(team_name)
    return team_names


def get_number_of_games_played(num_teams):
    while True:
        games_played = int(input("enter the number of games played by each team: "))
        if games_played >= num_teams - 1:
            break
        else:
            print("Invalid number of games, all teams must play at least once against the other teams")
    return games_played


def get_team_wins(team_names,games_played):
    team_wins = []
    for team in team_names:
        while True:
            wins = int(input(f"Enter the number of wins of Team {team}: "))
            if wins > games_played:
                print("Maximum number of wins is {games_played} , try again")
            elif wins < 0 :
                print("Minimum number of wins is 0, try again")
            else:
                break
        team_wins.append((team, wins))
    return team_wins

def get_second_item(item):
    return item[1]


num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

sorted_teams = sorted(team_wins, key= get_second_item)
games_to_be_played = len(sorted_teams) // 2

game_pairings = []

for games in range(games_to_be_played):
    home_team = sorted_teams[games][0]
    away_team = sorted_teams[num_teams-1-games][0]
    game_pairings.append([home_team,away_team])

for pairing in game_pairings:
    home_team , away_team = pairing
    print(f"Home: {home_team} Vs Away: {away_team}")
