def does_attack_hit(attack_roll, armor_class):
    return attack_roll!=0 or attack_roll>= armor_class or attack_roll==20
    

print(does_attack_hit(10,20))