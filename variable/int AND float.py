def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword +arrow + spear+ dagger + fireball
    average_damage = (sword +arrow + spear+ dagger + fireball)/5
    return total_damage, average_damage

print(calculate_damage(5,5,7,10,8))