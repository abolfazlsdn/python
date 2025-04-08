def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name== high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

print(check_high_score(0,10))

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        print("high")
    elif player_name == low_scoring_player_name:
        print("low")
    else:
        print("neither")
print(check_high_score(10,0,0))
