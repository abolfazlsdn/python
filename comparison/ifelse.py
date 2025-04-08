def player_status(health):
    if health== 0:
        print("dead")
    elif health<=5:
        print("injured")
    else:
        print("healthy")

player_status(0)