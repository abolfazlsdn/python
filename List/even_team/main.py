def split_players_into_teams(players):
    players_even = players[::2]
    players_odd = players[1::2]
    return players_even, players_odd