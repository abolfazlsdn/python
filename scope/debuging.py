def take_magic_damage(health, resist, amp, spell_power):
    final_damage = amp * spell_power
    last_damage =  final_damage - resist
    new_health = health - last_damage
    return new_health


print(take_magic_damage(1000,300,100,5))
