def update_player_score(current_score, increment):
    current_score -= increment
    return current_score

print(update_player_score(100,5))

def get_hurt(current_health, damage):
    current_health -= damage
    return current_health
print(get_hurt(100,50))