def get_most_common_enemy(enemies_dict):
    commen_enemy=None
    max_count=float("-inf")
    for enemy, count in enemies_dict.items():
        if count > max_count:
            max_count = count
            commen_enemy = enemy
    return commen_enemy


