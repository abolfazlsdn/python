glorfindel= 0b0001
galadriel = 0b0010
elendil = 0b0000
elrond = 0b0000
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond


print(calculate_guild_perms(glorfindel, galadriel, elendil, elrond))
