// Assignment 2
def group_players_by_position(squads_list):

    players_dict_list = players_as_dictionaries(squads_list)

    position_dict = {}
    
    for player in players_dict_list:
        position = player['position']
        if position not in position_dict:
            position_dict[position] = []
        position_dict[position].append(player)
    
    return position_dict
